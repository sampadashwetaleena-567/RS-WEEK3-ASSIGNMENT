#Noise Removal System of the image
import cv2

# Load Image
img = cv2.imread("noisy_img.png")
img = cv2.resize(img, (640, 480))

# Check image loaded successfully
if img is None:
    print("Image not found")

else:

    # Noise Removal using Gaussian Blur
    denoised = cv2.GaussianBlur(img, (5, 5), 0)

    # Calculate dimensions
    height, width = img.shape[:2]

    # Total pixels
    total_pixels = height * width

    print("Height :", height)
    print("Width  :", width)
    print("Total Pixels :", total_pixels)

    # Save output image
    cv2.imwrite("denoised_image.png", denoised)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Denoised Image", denoised)

    cv2.waitKey(0)
    cv2.destroyAllWindows()