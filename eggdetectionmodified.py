import numpy as np
import cv2

def reScaleFrame(frame, percent=75):
    width = int(frame.shape[1] * percent // 100)
    height = int(frame.shape[0] * percent // 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

img_path = r'C:\Users\shent\Documents\Sem 6\Computer Vision\Eggs\Testing photos\Test_enhanced.jpg'
frame = cv2.imread(img_path)

frame40 = reScaleFrame(frame, percent=40)

gray = cv2.cvtColor(frame40, cv2.COLOR_BGR2GRAY)

_, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, _ = cv2.findContours(bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

min_contour_area = 100  # Adjust this threshold as needed
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

if filtered_contours:
    largest_contour = max(filtered_contours, key=cv2.contourArea)
    (x, y, w, h) = cv2.boundingRect(largest_contour)
    cv2.rectangle(frame40, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Detected Egg", frame40)
cv2.waitKey(0)
cv2.destroyAllWindows()