import streamlit as st
import cv2
import numpy as np
import yolov5
import time
import requests



st.title("Garbage Detection and Classification from Image")


st.sidebar.header("Configuration")

api_endpoint = st.sidebar.text_input(
    "API Endpoint URL",
    "http://<replace-with-your-ip-address>/classification",
    help="Replace <replace-with-your-ip-address> with your actual API endpoint URL (e.g., http://192.168.1.100:5000/classification)"
)


@st.cache_resource
def load_yolov5_model():
    print("Loading YOLOv5 model...") 



    model = yolov5.load('keremberke/yolov5s-garbage', device='cpu')

    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 1000 # Maximum number of detections per image

    print("Model loaded.")
    return model

model = load_yolov5_model()


st.write("Upload an image containing garbage for detection and classification.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)


    frame = cv2.imdecode(file_bytes, 1) 


    st.subheader("Detection Results")

   
    results = model(frame, size=600)
    predictions = results.pred[0] 

    detected_labels = set() 


    for det in predictions:
        x1, y1, x2, y2, score, category = det
        category = int(category)
        label = model.names[category] 

        detected_labels.add(label)

      
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'{label} {score:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

 
    classification_result = 2 # Default to Anorganik

    if 'biodegradable' in detected_labels:
         classification_result = 1 # Change to Organik if 'biodegradable' is detected

    if detected_labels: 
        data_payload = {
            "result": classification_result
        }

        st.write(f"Detected Labels: {', '.join(detected_labels)}") 
        st.write(f"Determined Classification: **{classification_result}**") 

        try:

            r = requests.post(
                url=api_endpoint,
                json=data_payload,
                headers={'Content-Type': 'application/json'},
                timeout=5 
            )
            r.raise_for_status() 

            st.success(f"Successfully sent data: {data_payload} to {api_endpoint}")
        

        except requests.exceptions.RequestException as e:
           
            st.error(f"Failed to send data to {api_endpoint}: {e}")
            print(f"Failed to send data to {api_endpoint}: {e}")
        except Exception as e:

            st.error(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred during request: {e}")

    else:

         st.write("No objects detected in the image.")
         classification_result = "No Detection" 
         st.write(f"Determined Classification: **{classification_result}**")




    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    st.image(rgb_frame, caption="Image with Detections", channels="RGB", use_column_width=True)

else:

    st.info("Please upload an image to start the detection.")