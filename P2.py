#Showing FPS of the feed seen in webcam

import cv2
import time

# Start Webcam
cap = cv2.VideoCapture(0)

# Previous frame time
prev_time = 0

# Image counter
img_count = 1

while True:

    success, frame = cap.read()

    if not success:
        break

    # Current time
    curr_time = time.time()

    # FPS Calculation
    fps = 1 / (curr_time - prev_time)

    prev_time = curr_time

    # Display FPS
    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show Webcam Feed
    cv2.imshow("Webcam Feed", frame)

    key = cv2.waitKey(1)

    # Save Image
    if key == ord('s'):

        filename = f"image_{img_count}.png"

        cv2.imwrite(filename, frame)

        print(f"{filename} saved successfully")

        img_count += 1

    # Exit Program
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()