#Drawing through Hand Gesture

import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Canvas
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Previous drawing point
prev_x = None
prev_y = None

# Smoothening
smooth_factor = 5

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            lm = []

            for id, landmark in enumerate(hand.landmark):
                cx = int(landmark.x * w)
                cy = int(landmark.y * h)

                lm.append((cx, cy))

            # Finger Detection

            thumb_up = lm[4][0] > lm[3][0]

            index_up = lm[8][1] < lm[6][1]

            middle_up = lm[12][1] < lm[10][1]

            ring_up = lm[16][1] < lm[14][1]

            pinky_up = lm[20][1] < lm[18][1]

            # Index fingertip
            x = lm[8][0]
            y = lm[8][1]

            # DRAW MODE
            # Only Index Finger Open

            if (index_up and
                    not middle_up and
                    not ring_up and
                    not pinky_up):

                cv2.putText(
                    frame,
                    "DRAW MODE",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                if prev_x is None:

                    prev_x = x
                    prev_y = y

                else:

                    smooth_x = prev_x + (x - prev_x) // smooth_factor
                    smooth_y = prev_y + (y - prev_y) // smooth_factor

                    cv2.line(
                       canvas,
                        (prev_x, prev_y),
                        (smooth_x, smooth_y),
                        (0, 255, 0),
                        5
                    )

                    prev_x = smooth_x
                    prev_y = smooth_y


            # STOP MODE
            # All Fingers Closed

            elif (not thumb_up and
                  not index_up and
                  not middle_up and
                  not ring_up and
                  not pinky_up):

                cv2.putText(
                    frame,
                    "STOP",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2
                )

                prev_x = None
                prev_y = None


            # ERASER MODE
            # All Fingers Open

            elif (thumb_up and
                  index_up and
                  middle_up and
                  ring_up and
                  pinky_up):

                cv2.putText(
                    frame,
                    "ERASER",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

                cv2.circle(
                    canvas,
                    (x, y),
                    40,
                    (0, 0, 0),
                    -1
                )

                prev_x = None
                prev_y = None

            # Draw Hand Landmarks
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

    else:

        prev_x = None
        prev_y = None

    # Merge Webcam + Canvas

    output = cv2.add(frame, canvas)

    cv2.imshow("Virtual Drawing Board", output)

    key = cv2.waitKey(1)

    # Save Drawing
    if key == ord('s'):
        cv2.imwrite("drawing.png", canvas)

        print("Drawing saved as drawing.png")

    # Exit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()