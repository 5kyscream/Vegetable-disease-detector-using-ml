import os
import json

# Path to your training folder
train_dir = 'dataset/train'

# Get sorted list of classes
class_names = sorted(os.listdir(train_dir))

print("✅ Classes found:", class_names)

# Save to JSON file
with open('class_names.json', 'w') as f:
    json.dump(class_names, f)

print("✅ Saved to class_names.json")
