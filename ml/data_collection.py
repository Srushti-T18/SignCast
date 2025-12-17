import cv2
import mediapipe as mp
import numpy as np
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

WORDS = ["HELLO", "HOW", "YOU", "REST"]
SEQUENCES = 30
FRAMES = 30

dataset_path = "dataset"
os.makedirs(dataset_path, exist_ok=True)

cap = cv2.VideoCapture(0)

for word in WORDS:
    print(f"Recording for word: {word}")
    all_samples = []

    for seq in range(SEQUENCES):
        frames = []
        print(f"Sample {seq+1}/{SEQUENCES}")

        for _ in range(FRAMES):
            ret, frame = cap.read()
            if not ret:
                continue

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(frame_rgb)

            landmarks = np.zeros(63)
            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                landmarks = np.array(
                    [[lm.x, lm.y, lm.z] for lm in hand.landmark]
                ).flatten()

            frames.append(landmarks)

            cv2.putText(frame, word, (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.imshow("Collecting ASL Data", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        all_samples.append(frames)

    np.save(os.path.join(dataset_path, f"{word}.npy"), np.array(all_samples))
    print(f"Saved {word}.npy")

cap.release()
cv2.destroyAllWindows()

