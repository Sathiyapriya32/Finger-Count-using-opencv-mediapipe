import cv2
import mediapipe as mp

# Initialize MediaPipe hands solution
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Function to count fingers
def count_fingers(hand_landmarks):
    # Tip landmarks: Thumb (4), Index (8), Middle (12), Ring (16), Little (20)
    # MCP landmarks: Thumb (2), Index (5), Middle (9), Ring (13), Little (17)
    finger_tips = [4, 8, 12, 16, 20]
    finger_mcps = [2, 5, 9, 13, 17]

    count = 0

    # Check thumb
    if hand_landmarks[finger_tips[0]].x < hand_landmarks[finger_mcps[0]].x:
        count += 1

    # Check other fingers
    for i in range(1, 5):
        if hand_landmarks[finger_tips[i]].y < hand_landmarks[finger_mcps[i]].y:
            count += 1

    return count

# OpenCV camera setup
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural (selfie-view) visualization
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(rgb_frame)

    total_fingers = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            total_fingers += count_fingers(hand_landmarks.landmark)

    # Display the total finger count on the frame
    cv2.putText(frame, f'Fingers: {total_fingers}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3, cv2.LINE_AA)

    cv2.imshow('Finger Count', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
