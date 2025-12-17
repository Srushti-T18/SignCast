#BEST VERSION ALL CORRECT NO HELLO GLITCH
import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import pyttsx3
import threading

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

model = load_model("sign_model.h5")
labels = np.load("labels.npy")

mp_hands = mp.solutions.hands
# Increased detection confidence to 0.8
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
sequence = []
last_spoken = "" 
consistency_counter = 0 
REQUIRED_CONSISTENCY = 5 #Increased to 15 frames (0.15 seconds of steady signing)

while True:
    ret, frame = cap.read()
    if not ret: break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()
        
        sequence.append(landmarks)
        sequence = sequence[-30:] # Keep window at 30
    else:
        # IMPORTANT: If no hand is seen, clear the sequence 
        # This prevents the model from predicting based on old "ghost" frames
        sequence = []
        consistency_counter = 0

    if len(sequence) == 30:
        input_data = np.array(sequence).reshape(1, 30, 63)
        prediction = model.predict(input_data, verbose=0)[0]
        
        predicted_word = labels[np.argmax(prediction)]
        confidence = np.max(prediction)

        # STRICTER: Only look at predictions with very high confidence
        if confidence > 0.95: 
            if predicted_word != "REST" and predicted_word != last_spoken:
                consistency_counter += 1
                
                if consistency_counter >= REQUIRED_CONSISTENCY:
                    threading.Thread(target=speak, args=(predicted_word,)).start()
                    last_spoken = predicted_word
                    consistency_counter = 0
            
            elif predicted_word == "REST":
                last_spoken = "" # Reset memory
                consistency_counter = 0
        else:
            # If confidence is low, don't count it towards consistency
            consistency_counter = 0

    cv2.putText(frame, f"Last Spoken: {last_spoken}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("SignCast", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()


