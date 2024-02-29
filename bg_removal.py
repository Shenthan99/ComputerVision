import cv2
import numpy as np
import pandas

# Load the image
img = cv2.imread(img_path)

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Thresholding to binarize the image
_, thresh_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Select the contour with the largest area (assuming it's the egg)
if contours:
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the egg region from the original image
    egg_region = img[y:y+h, x:x+w]

    # Create a mask for the egg region
    mask = np.zeros_like(gray_img)
    cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Apply the mask to remove the background
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    # Calculate the centroid of the egg
    M = cv2.moments(largest_contour)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    # Calculate the shift needed to center the egg
    shift_x = img.shape[1] // 2 - cx
    shift_y = img.shape[0] // 2 - cy

    # Translate the egg to the center of the image
    translated_img = np.roll(masked_img, shift_x, axis=1)
    translated_img = np.roll(translated_img, shift_y, axis=0)

    # Display the result
    cv2.imshow("Egg Detection and Centering", translated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No contours found. Unable to detect the egg.")