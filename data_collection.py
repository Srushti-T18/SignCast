import cv2
import mediapipe as mp
import numpy as np
import os

# Configuration
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Your New Word List
WORDS = ["HELLO", "HOW", "YOU", "THANK YOU", "OUR", "TEAM", "NAME", "IS", "ANYHOW", "THIS", "PROJECT", "HOPE", "LIKE", "REST"]
SEQUENCES = 30 # Samples per hand (30 Right + 30 Left = 60 total)
FRAMES = 30
dataset_path = "dataset"

os.makedirs(dataset_path, exist_ok=True)
cap = cv2.VideoCapture(0)

for word in WORDS:
    # We will record for both hands to make the model robust
    for hand_type in ["RIGHT", "LEFT"]:
        print(f"--- Recording {word} for {hand_type} hand ---")
        all_samples = []

        for seq in range(SEQUENCES):
            frames = []
            
            # Pause between samples to let you reposition
            while True:
                ret, frame = cap.read()
                cv2.putText(frame, f"Ready? {word} ({hand_type}) Sample {seq+1}. Press 'S' to Start", 
                            (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                cv2.imshow("SignCast Data Collection", frame)
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break

            # Actual Recording
            for f_idx in range(FRAMES):
                ret, frame = cap.read()
                if not ret: continue

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(frame_rgb)

                landmarks = np.zeros(63)
                if result.multi_hand_landmarks:
                    hand = result.multi_hand_landmarks[0]
                    landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()

                frames.append(landmarks)

                # Visual Feedback
                cv2.putText(frame, f"RECORDING {word}: {f_idx}/{FRAMES}", (20, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                cv2.imshow("SignCast Data Collection", frame)
                cv2.waitKey(1)

            all_samples.append(frames)

        # Save as word_RIGHT.npy and word_LEFT.npy
        save_name = f"{word}_{hand_type}.npy"
        np.save(os.path.join(dataset_path, save_name), np.array(all_samples))
        print(f"Saved {save_name}")

cap.release()
cv2.destroyAllWindows()