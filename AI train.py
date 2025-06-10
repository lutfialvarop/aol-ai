import torch
from ultralytics import YOLO


data_yaml_path = 'C:\\Coding\\Python\\GARBAGE CLASSIFICATION 3.v2-gc1.yolov5pytorch\\data.yaml' 

model_name = 'keremberke/yolov5s-garbage.pt' 


device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO(model_name)  
model.to(device)  

# Set training parameters (you can adjust these)
epochs = 10  # Number of training epochs
imgsz = 640  # Image size (pixels)
batch_size = 16  # Batch size
# Train the model
results = model.train(data=data_yaml_path,
                     epochs=epochs,
                     imgsz=imgsz,
                     batch=batch_size)

# Print some information about the training (optional)
print(f"Training complete. Results saved to {results.save_dir}")