import cv2
import numpy as np

cap = cv2.VideoCapture(0)

saved = False

while True:

    success, frame = cap.read()

    if not success:
        break


    # Fix Mirror Effect

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape


    # Half Size Grayscale

    half = cv2.resize(frame, (w // 2, h // 2))

    gray_half = cv2.cvtColor(
        half,
        cv2.COLOR_BGR2GRAY
    )

    cv2.imshow(
        "Half Size Grayscale",
        gray_half
    )


    # Top Left : Original

    original = cv2.resize(
        frame,
        (w // 2, h // 2)
    )


    # Top Right : Vertical Flip

    flipped = cv2.flip(
        original,
        0
    )


    # Bottom Left : HSV

    hsv = cv2.cvtColor(
        original,
        cv2.COLOR_BGR2HSV
    )

    hsv = cv2.cvtColor(
        hsv,
        cv2.COLOR_HSV2BGR
    )


    # Bottom Right : Red Channel Only

    b, g, r = cv2.split(original)

    zeros = np.zeros_like(r)

    red_only = cv2.merge(
        [zeros, zeros, r]
    )


    # Create 4 Panel Window

    top_row = np.hstack(
        [original, flipped]
    )

    bottom_row = np.hstack(
        [hsv, red_only]
    )

    final_display = np.vstack(
        [top_row, bottom_row]
    )

    cv2.imshow(
        "Four Panel Display",
        final_display
    )


    # Channel Split
    cv2.imshow("Blue Channel", b)

    cv2.imshow("Green Channel", g)

    cv2.imshow("Red Channel", r)


    # Remove Green Channel

    merged_without_green = cv2.merge(
        [b, zeros, r]
    )

    cv2.imshow(
        "Without Green Channel",
        merged_without_green
    )

    # Save Once
    if not saved:

        cv2.imwrite(
            "merged_without_green.png",
            merged_without_green
        )

        saved = True

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()