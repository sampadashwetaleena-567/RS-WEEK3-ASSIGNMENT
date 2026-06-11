import cv2
import numpy as np

# Read image
img = cv2.imread("lake_img.png")
img = cv2.resize(img, (640, 480))

if img is None:
    print("Image not found")

else:

    # Split channels
    b, g, r = cv2.split(img)

    # Display channels
    cv2.imshow("Blue Channel", b)
    cv2.imshow("Green Channel", g)
    cv2.imshow("Red Channel", r)

    # Remove Green channel
    zero = np.zeros_like(g)

    merged_img = cv2.merge([b, zero, r])

    # Show merged image
    cv2.imshow("Without Green Channel", merged_img)

    # Save image
    cv2.imwrite(
        "without_green_channel.png",
        merged_img
    )

    print("Image Saved Successfully")

    cv2.waitKey(0)
    cv2.destroyAllWindows()