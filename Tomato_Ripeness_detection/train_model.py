import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from utils.data_utils import load_images_labels

# Paths
image_folder = "dataset/Images"
label_folder = "dataset/labels"

# Load data
X, y = load_images_labels(image_folder, label_folder)

if len(X) == 0:
    raise Exception("❌ No images loaded. Please check dataset paths and image format.")

X_flat = X.reshape(X.shape[0], -1)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_flat, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n📋 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("model", exist_ok=True)
with open("model/logistic_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n✅ Model trained and saved to model/logistic_model.pkl")
