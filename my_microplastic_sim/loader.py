import os
import pandas as pd

def load_excel_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found!")
        return None
    try:
        df = pd.read_excel(file_path)
        return df.iloc[:-1]
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None
