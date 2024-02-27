import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd

class SpreadsheetHandler:
    def __init__(self) :
        self.UserDataFrame = None
    
    def process_spreadsheet(self, file_path) :
        try:
            if file_path.endswith('.json') :
                self.UserDataFrame = pd.read_json(file_path)
            elif file_path.endswith('.xlsx') :
                self.UserDataFrame = pd.read_excel(file_path)
            elif file_path.endswith('.xls') :
                self.UserDataFrame = pd.read_excel(file_path)
            elif file_path.endswith('.csv') :
                self.UserDataFrame = pd.read_csv(file_path)
            else:
                raise ValueError("Unsupported file format. Please provide a .json, .xlsx, .xls, or .csv file.")
            
            return True
        
        except Exception as e :
            print(f"Error: {e}")
            self.df = None
            return False

handler = SpreadsheetHandler()
file_path = input("Enter the path to the spreadsheet file: ")
if handler.accept_spreadsheet(file_path) :
    print("Spreadsheet loaded successfully:")
    print(handler.df)
else:
    print("Failed to load DataFrame.")


class DataValidator:
    """Handles data validation tasks."""
    
    def validate_format(self, df: pd.DataFrame) -> bool:
        """Checks if the dataframe format matches the expected schema."""
        # Implementation for validating data format
        pass

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Identifies outliers in the dataframe."""
        # Implementation for detecting outliers
        pass

class DataCleaner:
    # Performs data cleaning operations.
    
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Imputes or removes missing values."""
        imputer = SimpleImputer(strategy='mean') # Example: mean imputation
        return pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    
    def convert_data_types(self, df: pd.DataFrame) -> pd.DataFrame:
        """Converts columns to more appropriate data types."""
        # Implementation for data type conversion
        pass

class DataPreprocessor:
    """Prepares data for machine learning models."""
    
    def normalize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Applies normalization to numerical columns."""
        scaler = StandardScaler()
        return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    def encode_categorical_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Encodes categorical variables using one-hot encoding."""
        encoder = OneHotEncoder()
        return pd.DataFrame(encoder.fit_transform(df).toarray(), columns=encoder.get_feature_names_out())

    def preprocess_text_data(self, column: pd.Series) -> pd.DataFrame:
        """Preprocesses text data in a given column."""
        vectorizer = CountVectorizer()
        return pd.DataFrame(vectorizer.fit_transform(column).toarray(), columns=vectorizer.get_feature_names_out())
