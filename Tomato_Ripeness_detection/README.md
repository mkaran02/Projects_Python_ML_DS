# 🍅 Tomato Ripeness Detection

A **Machine Learning** project that classifies tomato ripeness as **Ripe** or **Unripe** using image data.  
Built with **Scikit-learn** (Logistic Regression) and deployed via **Streamlit** for interactive predictions.

---

## 🚀 Features

- Upload a tomato image → Get instant prediction (Ripe/Unripe).
- Simple yet effective **Logistic Regression model**.
- Custom dataset with labeled tomato images.
- End-to-end workflow: **Training → Evaluation → Deployment**.

---

## 🛠 Tech Stack

- **Python 3**
- **Libraries**: Scikit-learn, Streamlit, NumPy, Pandas, OpenCV
- **Model**: Logistic Regression
- **Deployment**: Streamlit Web App

---

## 📂 Project Structure

Tomato_Ripeness_detection/
│-- app.py # Streamlit web app
│-- train_model.py # Model training script
│-- model/ # Saved trained model (logistic_model.pkl)
│-- dataset/
│ ├── Images/ # Tomato images
│ └── labels/ # Corresponding label files
│-- utils/
│ └── data_utils.py # Preprocessing + image loading functions


---

## ⚡ How It Works

1. **Training**
   - Preprocess dataset (images + labels).
   - Flatten images → train logistic regression.
   - Save trained model (`model/logistic_model.pkl`).

2. **Prediction**
   - Upload tomato image via Streamlit UI.
   - Model classifies as **Ripe** or **Unripe**.

---

## 🏗 Setup & Run


```
1. Clone Repo
git clone https://github.com/mkaran02/Projects_Python_ML_DS.git
cd Projects_Python_ML_DS/Tomato_Ripeness_detection
2. Install Dependencies
pip install -r requirements.txt
3. Train Model (if not already trained)
python train_model.py
4. Run Streamlit App
streamlit run app.py
Access at http://localhost:8501

📊 Dataset
Custom tomato dataset with Images and labels folders.

Structure:
dataset/
├── Images/
└── labels/
