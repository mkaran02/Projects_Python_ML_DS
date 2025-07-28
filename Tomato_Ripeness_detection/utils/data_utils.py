import cv2
import os
import numpy as np
import glob

def load_images_labels(image_folder, label_folder):
    images, labels = [], []

    # Supported image types
    extensions = ('*.jpg', '*.jpeg', '*.png')
    image_paths = []
    for ext in extensions:
        image_paths.extend(glob.glob(os.path.join(image_folder, ext)))

    print(f"🔍 Found {len(image_paths)} images in {image_folder}")

    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is None:
            print(f"⚠️ Could not read image: {img_path}")
            continue

        img = cv2.resize(img, (224, 224))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)

        filename = os.path.basename(img_path).split('.')[0]
        label_path = os.path.join(label_folder, filename + ".txt")

        if os.path.exists(label_path):
            with open(label_path, "r") as f:
                content = f.readlines()
            class_labels = set([int(line.split()[0]) for line in content])
            labels.append(1 if 1 in class_labels else 0)
        else:
            print(f"⚠️ Missing label file for: {filename}")
            continue

    print(f"✅ Loaded {len(images)} images and {len(labels)} labels")
    return np.array(images), np.array(labels)

def preprocess_image(image_path):
    import cv2
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_flat = img.reshape(1, -1)
    return img, img_flat
