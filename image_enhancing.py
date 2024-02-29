import cv2
import numpy as np

# File path of the image
image_path = r"C:\Users\shent\Documents\Sem 6\Computer Vision\Eggs\Testing photos\IMG_1306.DNG"

# Load the image
img = cv2.imread(image_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load the image. Please check the file path.")
else:
    # Increase sharpness
    sharpen_kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
    sharpened_img = cv2.filter2D(img, -1, sharpen_kernel)

    # Increase shadows
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0    # Brightness control (0-100)
    shadows_img = cv2.convertScaleAbs(sharpened_img, alpha=alpha, beta=beta)

    # Save the enhanced image
    output_path = r"C:\Users\shent\Documents\Sem 6\Computer Vision\Eggs\Testing photos\IMG_1306_enhanced.jpg"
    cv2.imwrite(output_path, shadows_img)

    print("Enhanced image saved successfully at:", output_path)