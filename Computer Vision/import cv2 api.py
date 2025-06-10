import cv2
import numpy as np
import yolov5
import time

# Load the YOLOv5s garbage detection model
model = yolov5.load('keremberke/yolov5s-garbage')
model.conf = 0.14  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 4  # Maximum number of detections per image

# Open webcam
#URL = "http://192.168.197.244"
#cap = cv2.VideoCapture(URL + ":81/stream")
cap = cv2.VideoCapture(0)  # Using local webcam

# The publish function is removed as it's for MQTT

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference (YOLOv5 takes BGR numpy arrays directly)
    results = model(frame, size=800)
    predictions = results.pred[0]  # Get predictions for the frame

    detected_labels = set()

    # Loop through detections
    for det in predictions:
        x1, y1, x2, y2, score, category = det
        category = int(category)
        label = model.names[category]  # Get original label from model

        # Add to detected labels set
        detected_labels.add(label)

        # Draw bounding boxes and labels on the frame
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f'{label} {score:.2f}', (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Publishing results block is removed

    # You can add code here to process the detected_labels set
    # For example, just printing them to the console:
    if detected_labels:
         print("Detected:", detected_labels)


    # Display result
    cv2.imshow("Trash Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# The client.disconnect() call is removed