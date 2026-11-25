# Face detection using a pre-trained Haar Cascade model in OpenCV.
# This detects face locations; it does not identify a person's identity.
# Install: pip install opencv-python
import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise SystemExit("Place an image named input.jpg in this folder.")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascade_path)
faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imwrite("face_detection_output.jpg", image)
print("Faces detected:", len(faces))
print("Output saved as face_detection_output.jpg")
