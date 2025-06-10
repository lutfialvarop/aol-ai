import cv2
import numpy as np
import yolov5
import time
import requests 


API_ENDPOINT = "http://192.168.101.247/classification"
# Example: API_ENDPOINT = "http://192.168.1.100:5000/classification"



model = yolov5.load('keremberke/yolov5s-garbage')
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 50  # Maximum number of detections per image

# --- Webcam Configuration ---
# Open webcam
#URL = "http://192.168.124.244"
#cap = cv2.VideoCapture(URL + ":81/stream")
cap = cv2.VideoCapture(0)  # Using local webcam


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from camera.")
        break


    results = model(frame, size=440)
    predictions = results.pred[0]  

    detected_labels = set() 

    for det in predictions:
        x1, y1, x2, y2, score, category = det
        category = int(category)
        label = model.names[category] 

        detected_labels.add(label)

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f'{label} {score:.2f}', (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


    if detected_labels:
        classification_result = 2 # Default to Anorganik

        if 'biodegradable' in detected_labels:
            classification_result = 1 # Change to Organik if 'biodegradable' is detected

        data_payload = {
            "result": classification_result
        }

        print(f"Detected Labels: {detected_labels}") 
        print(f"Sending Classification: {classification_result}") 

        try:
            r = requests.post(
                url=API_ENDPOINT,
                json=data_payload,
                headers={'Content-Type': 'application/json'},
                timeout=5 
            )

            r.raise_for_status()

            print(f"Successfully sent data: {data_payload} to {API_ENDPOINT}")
    
        except requests.exceptions.RequestException as e:

            print(f"Failed to send data to {API_ENDPOINT}: {e}")
        except Exception as e:

            print(f"An unexpected error occurred: {e}")
    else:

        pass 


    cv2.imshow("Trash Detection", frame)

    time.sleep(3)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        

cap.release()
cv2.destroyAllWindows()