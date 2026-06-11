#LED Indicator through pinch

import cv2
import mediapipe as mp
import math
import time

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# LED state
led_on = False

# Toggle control
last_toggle_time = 0
cooldown = 0.5

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            h, w, c = frame.shape

            # Thumb tip = 4
            thumb = hand.landmark[4]

            # Index tip = 8
            index = hand.landmark[8]

            x1 = int(thumb.x * w)
            y1 = int(thumb.y * h)

            x2 = int(index.x * w)
            y2 = int(index.y * h)

            # Draw points
            cv2.circle(frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

            # Distance
            distance = math.hypot(x2 - x1, y2 - y1)

            cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)

            current_time = time.time()

            # Pinch detected
            if distance < 40:

                if current_time - last_toggle_time > cooldown:

                    led_on = not led_on

                    last_toggle_time = current_time

    # LED Indicator
    if led_on:

        color = (0, 255, 0)
        text = "LED ON"

    else:

        color = (0, 0, 255)
        text = "LED OFF"

    cv2.circle(
        frame,
        (80, 80),
        30,
        color,
        cv2.FILLED
    )

    cv2.putText(
        frame,
        text,
        (130, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    cv2.imshow(
        "LED Toggle System",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()