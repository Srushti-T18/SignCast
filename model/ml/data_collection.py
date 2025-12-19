import cv2
import mediapipe as mp
import numpy as np
import os
import json

# Setup Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Paths
video_folder = "./archive/videos/" # Your path to the 12k videos
dataset_path = "dataset"
os.makedirs(dataset_path, exist_ok=True)

# Dataset Config
MAX_WORDS = 1000000000 # Limit to first 100 words for now
TARGET_FRAMES = 30 # Match your live_test.py window size

with open('./archive/WLASL_v0.3.json', 'r') as file:
    data = json.load(file)

# ... (imports and setup same as before)

# RESUME CONFIG
RESUME_VIDEO_ID = "46733" # Use string because JSON IDs are often strings
found = False 

# Iterate through words (glosses)
for entry_idx, entry in enumerate(data):
    if entry_idx >= MAX_WORDS:
        break
    
    word = entry["gloss"]
    print(f"Processing word: {word}")

    # Iterate through every video instance for this word
    for instance in entry["instances"]:
        video_id = str(instance["video_id"]) # Ensure string comparison
        
        # If we haven't reached the resume point yet, skip
        if not found:
            if video_id == RESUME_VIDEO_ID:
                found = True
                print(f"--- RESUMING FROM VIDEO {video_id} ---")
            else:
                continue # Skip this instance

        # --- DATA EXTRACTION START ---
        v_path = os.path.join(video_folder, f"{video_id}.mp4")
        
        if not os.path.exists(v_path):
            print(f"File missing: {v_path}")
            continue

        cap = cv2.VideoCapture(v_path)
        start_frame = instance["frame_start"]
        end_frame = instance["frame_end"]
        
        cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, start_frame - 1))
        
        frames_data = []
        for f_idx in range(TARGET_FRAMES):
            ret, frame = cap.read()
            landmarks = np.zeros(63)
            
            if ret:
                current_pos = cap.get(cv2.CAP_PROP_POS_FRAMES)
                # If segment is finished, pad with zeros
                if end_frame != -1 and current_pos > end_frame:
                    pass 
                else:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    result = hands.process(frame_rgb)
                    if result.multi_hand_landmarks:
                        hand = result.multi_hand_landmarks[0]
                        landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()

                    cv2.putText(frame, f"Word: {word} ID: {video_id}", (10, 30), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.imshow("WLASL Extraction", frame)
            
            frames_data.append(landmarks)
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                cap.release()
                cv2.destroyAllWindows()
                exit() # Proper exit on 'q'

        save_name = f"{word.upper()}_{video_id}.npy"
        np.save(os.path.join(dataset_path, save_name), np.array(frames_data))
        print(f"Saved: {save_name}")
        cap.release()

cv2.destroyAllWindows()

cv2.destroyAllWindows()