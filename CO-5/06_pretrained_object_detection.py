# Object detection with a pre-trained YOLO model using Ultralytics
# Install: pip install ultralytics
# Put an image named input.jpg in this folder.
from ultralytics import YOLO
from pathlib import Path

image_path = Path("input.jpg")
if not image_path.exists():
    raise SystemExit("Place an image named input.jpg in this folder.")
model = YOLO("yolov8n.pt")  # Downloads pretrained weights on first run
results = model(str(image_path))
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        print(model.names[class_id], "confidence:", round(confidence, 3))
    result.save(filename="detected_output.jpg")
print("Annotated image saved as detected_output.jpg")
