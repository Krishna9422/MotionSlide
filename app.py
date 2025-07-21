import cv2
import mediapipe as mp
import pyautogui
import keyboard
import numpy as np
import time

# Setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
cursor_frozen = False
prev_click = 0

def get_finger_status(hand_landmarks):
    fingers = []
    tips = [4, 8, 12, 16, 20]

    for i in range(1, 5):
        if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[tips[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Thumb (x-coord for horizontal detection)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.insert(0, 1)
    else:
        fingers.insert(0, 0)

    return fingers  # [thumb, index, middle, ring, pinky]

def is_fist(finger_status):
    return finger_status == [0, 0, 0, 0, 0]

def is_palm(finger_status):
    return finger_status == [1, 1, 1, 1, 1]

def are_fingers_touching(lm, finger1_id, finger2_id):
    x1, y1 = lm[finger1_id].x, lm[finger1_id].y
    x2, y2 = lm[finger2_id].x, lm[finger2_id].y
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance < 0.05  # Adjust threshold if needed

def is_index_up(finger_status):
    return finger_status[1] == 1 and sum(finger_status) == 1

def is_middle_up(finger_status):
    return finger_status[2] == 1 and sum(finger_status) == 1

freeze_position = (0, 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmark, hand_handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            hand_label = hand_handedness.classification[0].label
            finger_status = get_finger_status(hand_landmark)

            cx = int(hand_landmark.landmark[9].x * w)
            cy = int(hand_landmark.landmark[9].y * h)
            screen_x = int(hand_landmark.landmark[9].x * screen_w)
            screen_y = int(hand_landmark.landmark[9].y * screen_h)

            # Right Hand - Cursor and click
            if hand_label == 'Right':
                if not cursor_frozen:
                    pyautogui.moveTo(screen_x, screen_y)

                if is_fist(finger_status):
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    filename = f"screenshot_{timestamp}.png"
                    pyautogui.screenshot(filename)
                    print(f"Screenshot saved: {filename}")
                    time.sleep(1)

                elif finger_status == [0, 1, 0, 0, 0] and time.time() - prev_click > 1:
                    pyautogui.rightClick()
                    prev_click = time.time()

                elif finger_status == [0, 0, 1, 0, 0] and time.time() - prev_click > 1:
                    pyautogui.leftClick()
                    prev_click = time.time()

                cursor_frozen = finger_status[0] == 0

            # Left Hand - Scroll, Win+Tab, Volume
            elif hand_label == 'Left':
                lm = hand_landmark.landmark

                if is_index_up(finger_status):
                    pyautogui.scroll(20)
                elif is_middle_up(finger_status):
                    pyautogui.scroll(-20)
                elif is_fist(finger_status):
                    keyboard.press('win')
                    keyboard.press_and_release('tab')
                    keyboard.release('win')
                    time.sleep(1)

                elif are_fingers_touching(lm, 8, 4):  # Index + Thumb
                    keyboard.send("volume up")

                elif are_fingers_touching(lm, 12, 4):  # Middle + Thumb
                   keyboard.press_and_release("volume down")

            mp_drawing.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
