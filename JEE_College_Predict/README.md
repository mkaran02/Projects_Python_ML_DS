# 🎓 JEE College Predictor (IIT & NIT)

A **Machine Learning-powered web application** to predict eligible **IIT and NIT colleges** based on your **JEE rank, category, quota, and gender pool**. Built with **Flask, HTML, CSS, and Scikit-learn**, it provides **closest 20 colleges (ambitious, match, safe)** using historical cutoff data.

---

## 🚀 Features

- **IIT & NIT Predictions**  
  Uses real JEE counseling data to show top 20 colleges around your rank.

- **Closest 20 Colleges Algorithm**  
  Shows **10 better, 10 worse, and exact match** colleges for realistic options.

- **Modern UI**  
  - Glassmorphism design  
  - Animated gradient hero section  
  - Floating label inputs  
  - Gradient buttons with hover effects  

- **Color-coded Results**  
  - Green = Exact Rank Match  
  - Yellow = Ambitious (Better rank)  
  - Blue = Safe (Worse rank)  

- **Responsive Design**  
  Works seamlessly on desktop and mobile.

---

## 🖼️ Screenshots

### **Homepage**
<img width="1203" height="475" alt="image" src="https://github.com/user-attachments/assets/72cec8f8-4fdb-42ea-9ac4-9280ce87110d" />


### **Results Page**

<img width="888" height="461" alt="image" src="https://github.com/user-attachments/assets/8d1ec0c2-fe8c-4b4a-9880-82af47f68351" />
<img width="1114" height="643" alt="image" src="https://github.com/user-attachments/assets/1b65e760-092d-4554-95b2-afdffff35f18" />


---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3 (Glassmorphism, Animations)  
- **Backend:** Flask (Python)  
- **ML Library:** Scikit-learn, Pandas, NumPy  
- **Model Persistence:** Joblib  
- **Data:** Historical JEE Cutoff Data (IITs & NITs)  

---

## ⚡ Workflow

1. **Input Details:** Enter JEE rank, category, quota, and gender pool.  
2. **Prediction Algorithm:**  
   - Filters data for selected category/quota/pool.  
   - Finds **20 closest colleges** (10 better, 10 worse) around your rank.  
3. **Results Display:**  
   - Sorted table with opening/closing ranks.  
   - Color-coded rows for better insights.  
4. **Download Option (Planned):** CSV of eligible colleges.

---

## 📊 Accuracy

<img width="512" height="317" alt="accuracy" src="https://github.com/user-attachments/assets/3d933175-b16b-471b-9c24-0ca208c56755" />

- Model trained on **historical JEE counseling data** (IIT + NIT).  
- Uses **rank proximity** rather than binary cutoff match — more **practical for counseling decisions**.  
- Provides **guidance, not official allotment guarantee** (official cutoffs may vary yearly).

---

## 📂 Project Structure

jee_college_predictor/
│-- app.py # Flask app entry
│-- data_processor.py # Data cleaning & preprocessing
│-- model_trainer.py # Model training & saving
│-- predictor.py # Prediction logic
│-- requirements.txt # Dependencies
│-- /data # Historical cutoff data (data.csv)
│-- /models # Trained model storage
│-- /templates # HTML templates (index, results)
│-- /static # CSS, images


## 🏗️ Setup & Installation

### **1. Clone Repository**
```bash
git clone https://github.com/your-username/JEE_College_Predictor.git
cd JEE_College_Predictor
2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

3. Install Dependencies
pip install -r requirements.txt

4. Add Data
Place your data.csv inside the data/ folder.

5. Run the App
python app.py
Open http://127.0.0.1:5000 in your browser.
