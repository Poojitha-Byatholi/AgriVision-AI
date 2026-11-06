import os

DATASET_DIR = "data/raw/train"

# Get only directories (class folders)
class_names = sorted([
    d for d in os.listdir(DATASET_DIR)
    if os.path.isdir(os.path.join(DATASET_DIR, d))
])

print("CLASS_NAMES = [")
for name in class_names:
    print(f'    "{name}",')
print("]")
