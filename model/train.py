import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint

# Load preprocessed data
X = np.load("X.npy")
y = np.load("y.npy")

print("X shape:", X.shape)
print("y shape:", y.shape)

# Build LSTM model
model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(X.shape[1], X.shape[2])),
    LSTM(64),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# Save best model
checkpoint = ModelCheckpoint(
    "sign_model.h5",
    monitor="loss",
    save_best_only=True,
    verbose=1
)

# Train model
model.fit(
    X, y,
    epochs=30,
    batch_size=16,
    validation_split=0.2,
    callbacks=[checkpoint]
)

print("✅ TRAINING COMPLETE — model saved as sign_model.h5")
