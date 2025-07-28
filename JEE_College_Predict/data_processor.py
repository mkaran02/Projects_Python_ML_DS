import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

class DataProcessor:
    def __init__(self, data_path):
        """Initialize data processor with the path to the dataset."""
        self.data_path = data_path
        self.label_encoders = {}
        
    def load_data(self):
        """Load the dataset from CSV file."""
        print(f"Loading data from {self.data_path}")
        self.data = pd.read_csv(self.data_path)
        return self.data
    
    def preprocess_data(self):
        """Preprocess the data for model training."""
        print("Preprocessing data...")
        # Drop unnecessary columns
        self.data.drop(columns=['id', 'institute_short', 'program_name'], inplace=True, errors='ignore')
        
        # Convert institute_type to binary
        self.data['institute_type'] = [0 if x == 'IIT' else 1 for x in self.data['institute_type']]
        
        # Convert pool to binary
        self.data['pool'] = [0 if x == 'Gender-Neutral' else 1 for x in self.data['pool']]
        
        # Convert program_duration to binary
        self.data['program_duration'] = [0 if x == '4 Years' else 1 for x in self.data['program_duration']]
        
        # Use label encoder for categorical variables
        categorical_cols = ['quota', 'degree_short', 'category']
        for col in categorical_cols:
            if col in self.data.columns:
                le = LabelEncoder()
                self.data[col] = le.fit_transform(self.data[col])
                self.label_encoders[col] = le
        
        return self.data
    
    def get_X_y(self):
        """Split data into features and target."""
        if not hasattr(self, 'data'):
            self.load_data()
            self.preprocess_data()
            
        y = self.data['is_preparatory']
        X = self.data.drop(columns='is_preparatory')
        
        return X, y
    
    def get_unique_categories(self):
        """Get unique categories from the original data."""
        if not hasattr(self, 'data'):
            self.load_data()
        
        return self.data['category'].unique().tolist()
    
    def get_categorical_mappings(self):
        """Return mappings of encoded categorical values to original values."""
        mappings = {}
        for col, le in self.label_encoders.items():
            mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))
        return mappings
    
    def get_colleges_by_rank(self, rank, category):
        """Get colleges where closing rank is >= the given rank for the specified category."""
        if not hasattr(self, 'data'):
            self.load_data()
        
        # Filter colleges by rank and category
        eligible_colleges = self.data[(self.data['closing_rank'] >= rank) & 
                                     (self.data['category'] == category)]
        
        if eligible_colleges.empty:
            return pd.DataFrame()
            
        # Get relevant columns for display
        result = eligible_colleges[['institute_type', 'institute_short', 'program_name', 
                                    'opening_rank', 'closing_rank', 'category']]
        
        # Sort by closing rank (highest rank first)
        result = result.sort_values(by='closing_rank', ascending=False)
        
        return result