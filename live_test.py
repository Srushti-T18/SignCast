import os
# Suppress all TF logs and oneDNN messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2
import mediapipe as mp
import numpy as np
import threading
import pyttsx3
import time
from tensorflow.keras.models import load_model

# --- CONFIGURATION ---
MODEL_PATH = "sign_model.h5"
LABELS_PATH = "labels.npy"
WINDOW_SIZE = 30
MIN_CONFIDENCE = 0.95
REQUIRED_CONSISTENCY = 5

# --- SHARED STATE ---
state = {
    "latest_sequence": None,
    "last_sign": "",
    "sentence_history": [],
    "running": True
}

model = load_model(MODEL_PATH)
labels = np.load(LABELS_PATH)

def speak_now(text):
    """Blocking speech with optimized human-like settings"""
    engine = pyttsx3.init()
    
    # 1. SELECT A BETTER VOICE
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Zira" in voice.name or "Hazel" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    
    # 2. SLOW DOWN THE RATE
    engine.setProperty('rate', 160)
    
    # 3. ADJUST VOLUME
    engine.setProperty('volume', 1.0)

    # 4. FORMAT TEXT FOR NATURAL INTONATION
    clean_text = text.strip().capitalize() + "."
    
    engine.say(clean_text)
    engine.runAndWait()

# Local bridge dictionary (Expand this as needed for your specific dataset)
LOCAL_BRIDGES = {
    ("how", "you"): "ARE",
    ("i", "hungry"): "AM",
    ("you", "hungry"): "ARE",
    ("i", "fine"): "AM",
    ("go", "school"): "TO",
    ("what", "name"): "is your"
}

def get_bridge_words(history, new_word):
    """
    Checks the local dictionary for grammatical bridges.
    """
    if not history: 
        return ""
    
    # Clean the input strings
    left_context = str(history[-1]).strip().lower()
    right_word = str(new_word).strip().lower()
    
    # Try local dictionary (Instant/Offline)
    if (left_context, right_word) in LOCAL_BRIDGES:
        return LOCAL_BRIDGES[(left_context, right_word)]
    
    return "" # No bridge word found locally

def ai_worker():
    consistency_counter = 0
    current_prediction = ""
    
    while state["running"]:
        if state["latest_sequence"] is not None:
            input_data = np.expand_dims(state["latest_sequence"], axis=0)
            prediction = model.predict(input_data, verbose=0)[0]
            idx = np.argmax(prediction)
            
            if prediction[idx] > MIN_CONFIDENCE:
                predicted_word = str(labels[idx])
                
                if predicted_word == "REST":
                    consistency_counter = 0
                elif predicted_word != state["last_sign"]:
                    if predicted_word == current_prediction:
                        consistency_counter += 1
                    else:
                        current_prediction = predicted_word
                        consistency_counter = 0
                    
                    if consistency_counter >= REQUIRED_CONSISTENCY:
                        # 1. Get the local bridge
                        bridge = get_bridge_words(state["sentence_history"], predicted_word)
                        
                        # 2. Localized Speech Flow
                        if bridge:
                            print(f"Local Bridge: {bridge}")
                            speak_now(bridge + ",") 
                            state["sentence_history"].append(bridge)
                            time.sleep(0.1) 
                        
                        print(f"Sign Detected: {predicted_word}")
                        speak_now(predicted_word.capitalize() + ".")
                        state["sentence_history"].append(predicted_word)

                        # 3. Cooldown logic
                        state["last_sign"] = predicted_word
                        consistency_counter = 0
                        time.sleep(0.1) 
            else:
                consistency_counter = 0
        time.sleep(0.01)

# Start logic thread
threading.Thread(target=ai_worker, daemon=True).start()

# --- MAIN UI LOOP ---
def main():
    cap = cv2.VideoCapture(0)
    # Replaced mp.solutions.hands with a more direct initialization 
    # compatible with standard MediaPipe versions.
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(model_complexity=0)
    sequence_data = []

    print("--- SignCast Local Active ---")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()
            sequence_data.append(landmarks)
            if len(sequence_data) > WINDOW_SIZE: sequence_data.pop(0)
            if len(sequence_data) == WINDOW_SIZE:
                state["latest_sequence"] = np.array(sequence_data)
        else:
            sequence_data.clear()
            state["latest_sequence"] = None

        # Display current sentence
        display_text = " ".join(state["sentence_history"])
        cv2.rectangle(frame, (0, 420), (640, 480), (0, 0, 0), -1)
        cv2.putText(frame, display_text, (20, 460), 1, 1.5, (255, 255, 255), 2)
        
        # Removed cv2.imshow and waitKey to prevent window opening
        # cv2.imshow("SignCast Local", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()