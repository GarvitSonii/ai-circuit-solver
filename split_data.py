import os
import shutil
import random

# Paths
dataset_dir = "data"   # contains class folders (e.g., cat/, dog/)
output_dir = "split_dataset"

# Ratios
train_ratio, val_ratio, test_ratio = 0.7, 0.15, 0.15

# Ensure output dirs exist
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Loop over each class
for class_name in os.listdir(dataset_dir):
    class_dir = os.path.join(dataset_dir, class_name)
    if not os.path.isdir(class_dir):
        continue

    images = os.listdir(class_dir)
    random.shuffle(images)

    n_total = len(images)
    n_train = int(train_ratio * n_total)
    n_val = int(val_ratio * n_total)

    train_imgs = images[:n_train]
    val_imgs = images[n_train:n_train + n_val]
    test_imgs = images[n_train + n_val:]

    # Copy files
    for split, img_list in [("train", train_imgs), ("val", val_imgs), ("test", test_imgs)]:
        split_class_dir = os.path.join(output_dir, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)
        for img in img_list:
            src = os.path.join(class_dir, img)
            dst = os.path.join(split_class_dir, img)
            shutil.copy(src, dst)

print("✅ Done! Dataset split into train/val/test.")
