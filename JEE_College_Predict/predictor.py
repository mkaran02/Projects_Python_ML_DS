import pandas as pd
import numpy as np

class CollegePredictor:
    def __init__(self, model, original_data_path):
        """Initialize predictor with trained model and original data."""
        self.model = model
        self.data = pd.read_csv(original_data_path)
    
    def get_eligible_colleges(self, rank, category, quota='AI', pool='Gender-Neutral'):
        """
        Return top 20 colleges closest to the user's rank (10 better, 10 worse).
        Exact matches are prioritized first.
        """
        # Filter dataset by user inputs
        data_filtered = self.data[
            (self.data['category'] == category) &
            (self.data['quota'] == quota) &
            (self.data['pool'] == pool)
        ].copy()

        # Calculate difference (positive = worse rank, negative = better rank)
        data_filtered['rank_diff'] = data_filtered['closing_rank'] - rank

        # Sort by absolute difference (closest first)
        data_filtered = data_filtered.reindex(
            data_filtered['rank_diff'].abs().sort_values().index
        )

        # Pick top 20 results
        result = data_filtered.head(20)

        # Select relevant columns
        result = result[['institute_type', 'institute_short', 'program_name',
                         'opening_rank', 'closing_rank', 'rank_diff']]

        return result

    def predict_eligibility(self, rank, category, quota='AI', pool='Gender-Neutral'):
        """
        Predict if the student is eligible for preparatory courses based on rank and category.
        
        Args:
            rank (int): JEE rank of the student
            category (str): Category of the student
            quota (str): Quota of the student
            pool (str): Pool of the student
            
        Returns:
            bool: True if eligible for preparatory courses, False otherwise
        """
        # Create a sample for prediction
        sample = pd.DataFrame({
            'year': [2021],  # Assuming current year
            'institute_type': [0],  # Assuming IIT
            'round_no': [1],  # Assuming round 1
            'quota': [quota],
            'pool': [0 if pool == 'Gender-Neutral' else 1],
            'program_duration': [0],  # Assuming 4 years
            'degree_short': ['B.Tech'],  # Assuming B.Tech
            'category': [category],
            'opening_rank': [rank - 100],  # Approximation
            'closing_rank': [rank]  # User's rank
        })
        
        # Make prediction
        prediction = self.model.predict(sample)
        
        return bool(prediction[0])
    
    def get_all_categories(self):
        """Get all available categories from the dataset."""
        return sorted(self.data['category'].unique().tolist())
    
    def get_all_quotas(self):
        """Get all available quotas from the dataset."""
        return sorted(self.data['quota'].unique().tolist())
    
    def get_all_pools(self):
        """Get all available pools from the dataset."""
        return sorted(self.data['pool'].unique().tolist())
