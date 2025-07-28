from flask import Flask, render_template, request
import os
from data_processor import DataProcessor
from model_trainer import ModelTrainer
from predictor import CollegePredictor

app = Flask(__name__)

DATA_PATH = "data/data.csv"
MODEL_PATH = "models/trained_model.pkl"

# Load model & predictor
def load_predictor():
    # Load or train model
    if os.path.exists(MODEL_PATH):
        model = ModelTrainer.load_model(MODEL_PATH)
    else:
        processor = DataProcessor(DATA_PATH)
        processor.load_data()
        processor.preprocess_data()
        X, y = processor.get_X_y()

        trainer = ModelTrainer(X, y)
        model, _, _ = trainer.train_model()

        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        trainer.save_model(MODEL_PATH)

    return CollegePredictor(model, DATA_PATH)

predictor = load_predictor()

categories = predictor.get_all_categories()
quotas = predictor.get_all_quotas()
pools = predictor.get_all_pools()

@app.route('/')
def index():
    return render_template('index.html', categories=categories, quotas=quotas, pools=pools)

@app.route('/predict', methods=['POST'])
def predict():
    rank = int(request.form['rank'])
    category = request.form['category']
    quota = request.form['quota']
    pool = request.form['pool']

    eligible_colleges = predictor.get_eligible_colleges(rank, category, quota, pool)

    return render_template('results.html', colleges=eligible_colleges.to_dict(orient='records'), rank=rank)

if __name__ == "__main__":
    app.run(debug=True)
