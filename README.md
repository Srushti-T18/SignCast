
# SignCast: Real-Time ASL-to-Speech Translation

**Developed by Team Anyhow**
*Samagra Agarwal, Srushti Talandage, and Bhoumik Sangle*

SignCast is a real-time accessibility tool designed to bridge the communication gap for the speech-impaired. By leveraging computer vision and deep learning, SignCast translates American Sign Language (ASL) gestures into spoken language instantaneously.

##  The Mission

For millions of individuals who rely on ASL, communicating with non-signers in real-time remains a significant challenge. SignCast provides a **software-based bridge**, converting complex hand movements into synthesized speech, empowering users to express themselves naturally in any environment.

##  Technical Architecture

SignCast uses a sophisticated pipeline to ensure that both the **shape** and the **motion** of signs are captured accurately.

1. **Input:** Real-time video stream processed at **30 FPS**.
2. **Landmark Extraction:** [MediaPipe](https://www.google.com/search?q=https://google.github.io/mediapipe/) extracts 21 3D hand landmarks per frame.
3. **Normalization:** To ensure the model is invariant to where the user is sitting, all landmarks are **normalized relative to the wrist** ().
4. **Temporal Processing:** A **Bi-Directional LSTM (Long Short-Term Memory)** network processes a sliding window of 30 frames to understand the motion.
5. **Classification:** A Softmax layer chooses the correct gloss from a vocabulary of **2,700 signs**.
6. **Output:** The predicted text is converted to audio via a **Text-to-Speech (TTS)** engine.

##  Dataset & Performance

* **Dataset:** [ASL Citizen](https://www.google.com/search?q=https://aslcitizen.microsoft.com/) (2,700+ distinct signs).
* **Data Split:** 60% Training | 25% Validation | 15% Testing.
* **Accuracy:** Achieved a final validation accuracy of **85.74%**.

##  Installation & Setup

**Prerequisites:** Python 3.10

```bash
# Clone the repository
git clone https://github.com/your-repo/SignCast.git

# Create a virtual environment
python3 -m venv signcast_env
source signcast_env/bin/activate

# Install dependencies
pip install tensorflow mediapipe opencv-python pandas numpy

```

##  Project Structure

```text
├── /models
│   ├── SignCast_best_model.h5  # Trained Bi-LSTM model
│   └── label_map.json          # Dictionary for 2,700 signs
├── data_loader.py              # Custom ASLDataGenerator
├── train_model.py              # Model architecture & training script
└── webcam_test.py              # Real-time inference & TTS integration

```

##  Future Roadmap

Team Anyhow is committed to expanding SignCast into a full-scale accessibility suite:

* **Custom Word Feature:** Allowing users to record and train personal idiosyncratic signs.
* **Subtitles:** Integrated overlay for video conferencing platforms.
* **Multi-Hand Support:** Expanding landmarks to include facial expressions and body pose for more nuanced translation.
