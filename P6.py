#Show the Kernel size
import cv2

# Start Webcam
cap = cv2.VideoCapture(0)

# Initial kernel size
kernel_size = 5

while True:

    success, frame = cap.read()

    if not success:
        break

    # Convert to Grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(
        gray,
        (kernel_size, kernel_size),
        0
    )

    # Canny Edge Detection
    edges = cv2.Canny(
        blur,
        100,
        200
    )

    # Display Blur Value
    cv2.putText(
        edges,
        f"Kernel : {kernel_size}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        255,
        2
    )

    cv2.imshow(
        "Dynamic Edge Detector",
        edges
    )

    key = cv2.waitKey(1)

    # Increase Blur
    if key == ord('w'):

        kernel_size += 2

        if kernel_size > 31:
            kernel_size = 31

    # Decrease Blur
    elif key == ord('s'):

        kernel_size -= 2

        if kernel_size < 3:
            kernel_size = 3

    # Exit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()