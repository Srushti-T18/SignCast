import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import pyttsx3

# Load trained model and labels
model = load_model("sign_model.h5")
labels = np.load("labels.npy")

# Text-to-speech
engine = pyttsx3.init()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
sequence = []

last_spoken = ""   #NEW: to prevent repeating same word

print("Show HELLO / HOW / YOU")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    landmarks = np.zeros(63)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()

    sequence.append(landmarks)

    if len(sequence) == 30:
        input_data = np.array(sequence).reshape(1, 30, 63)
        prediction = model.predict(input_data, verbose=0)[0]

        predicted_word = labels[np.argmax(prediction)]
        confidence = np.max(prediction)

        # SPEAK ONLY IF WORD CHANGES
        if confidence > 0.8 and predicted_word != last_spoken:
            print(f"Predicted: {predicted_word} ({confidence:.2f})")
            engine.say(predicted_word)
            engine.runAndWait()
            last_spoken = predicted_word

        sequence = []

    cv2.imshow("SignCast - Live Sign to Speech", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
