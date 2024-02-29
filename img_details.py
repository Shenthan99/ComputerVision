import cv2

# File path of the image
image_path = r"C:\Users\shent\Documents\Sem 6\Computer Vision\Eggs\Testing photos\IMG_1306.DNG"

# Load the image
img = cv2.imread(image_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load the image. Please check the file path.")
else:
    # Get image dimensions (height x width) ~ Image size
    height, width = img.shape[:2]
    print("Size of the image:", width, "x", height)

    # Get image resolution
    resolution = img.shape
    print("Resolution of the image:", resolution)

    # Check if the image is grayscale or color
    if len(img.shape) == 2:
        print("Image is grayscale")
    elif len(img.shape) == 3:
        print("Image is color")

    # Get pixel intensity values (for the first pixel)
    pixel_intensity = img[0, 0]
    print("Pixel intensity values for the first pixel:", pixel_intensity)