import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

class ModelTrainer:
    def __init__(self, X, y):
        """Initialize model trainer with features and target."""
        self.X = X
        self.y = y
        self.model = None
        
    def train_model(self, test_size=0.2, random_state=42):
        """Train a logistic regression model."""
        print("Training model...")
        
        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state
        )
        
        # Train logistic regression model
        self.model = LogisticRegression(C=10, max_iter=1000)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        print(f"Model accuracy: {accuracy:.4f}")
        print("Classification report:")
        print(report)
        
        return self.model, accuracy, report
    
    def save_model(self, filepath):
        """Save the trained model to disk."""
        if self.model is None:
            raise ValueError("Model has not been trained yet.")
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        print(f"Saving model to {filepath}")
        joblib.dump(self.model, filepath)
        
    @staticmethod
    def load_model(filepath):
        """Load a trained model from disk."""
        print(f"Loading model from {filepath}")
        return joblib.load(filepath)