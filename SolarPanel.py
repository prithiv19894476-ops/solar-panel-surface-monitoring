import cv2
import numpy as np

# Read the solar panel image
image = cv2.imread("solar_panel.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Remove noise using blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Detect edges (cracks or scratches)
edges = cv2.Canny(blur, 50, 150)

# Detect dust spots using threshold
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Calculate defect percentage
defect_pixels = np.sum(thresh == 255)
total_pixels = thresh.size
defect_percentage = (defect_pixels / total_pixels) * 100

# Classify severity
if defect_percentage < 5:
    severity = "Low"
elif defect_percentage < 15:
    severity = "Medium"
else:
    severity = "High"

print("Defect Percentage:", defect_percentage)
print("Severity:", severity)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Edge Detection", edges)
cv2.imshow("Defect Detection", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()