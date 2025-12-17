import os
import numpy as np
from sklearn.preprocessing import LabelBinarizer

dataset_path = "dataset"
words = [f.split(".")[0] for f in os.listdir(dataset_path) if f.endswith(".npy")]

X = []
y = []

for word in words:
    data = np.load(os.path.join(dataset_path, f"{word}.npy"))  # shape: (num_samples, frames, 63)
    for sample in data:
        X.append(sample)
        y.append(word)

X = np.array(X)
y = np.array(y)

# One-hot encode labels
lb = LabelBinarizer()
y = lb.fit_transform(y)

# Save processed data
np.save("X.npy", X)
np.save("y.npy", y)
np.save("labels.npy", lb.classes_)
print("Preprocessing complete.")
