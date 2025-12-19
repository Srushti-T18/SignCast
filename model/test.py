import numpy as np

# Load current labels
labels = list(np.load("labels.npy"))

# Add a label for the 4th index (Index 3)
if len(labels) == 3:
    labels.append("IDLE") # You can name this "NOTHING" or "IDLE"
    np.save("labels.npy", np.array(labels))
    print(f"Updated labels: {labels}")
else:
    print("Labels already have 4 or more items.")