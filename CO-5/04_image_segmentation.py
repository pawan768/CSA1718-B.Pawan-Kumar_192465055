# Image segmentation using OpenCV thresholding
# Install: pip install opencv-python
import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise SystemExit("Place an image named input.jpg in this folder.")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("segmented_output.png", segmented)
print("Segmentation saved as segmented_output.png")
