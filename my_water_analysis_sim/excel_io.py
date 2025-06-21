import os.path
import pandas as pd

def load_excel_data(file_path):
    """Load data from Excel file and return as DataFrame"""
    # Step 1: Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found!")
        return None
    try:
        # Step 2: Read Excel file
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        # Step 3: Handle errors during file reading
        print(f"Error reading Excel file: {e}")
        return None
    
def calculate_total_length_by_type(excel_file_path, length_column="Länge", type_column="Gewässertyp"):
    """
    Calculate the total length of each water body type from an Excel sheet,
    excluding the last two rows.
    
    Parameters:
    excel_file_path (str): Path to the Excel file
    length_column (str): Name of the column containing length values
    type_column (str): Name of the column containing water body types
    
    Returns:
    pd.DataFrame: A DataFrame with water body types and their total lengths
    """
    try:
        # Step 1: Read the Excel file
        df = pd.read_excel(excel_file_path)
        
        # Step 2: Exclude the last two rows (often summary or notes)
        df = df.iloc[:-2]

        # Step 3: Ensure the required columns exist
        if length_column not in df.columns or type_column not in df.columns:
            raise ValueError(f"Required columns '{length_column}' or '{type_column}' not found in the Excel file.")
        
        # Step 4: Convert length values to numeric, handling potential formatting issues
        df[length_column] = pd.to_numeric(df[length_column], errors='coerce')
        
        # Step 5: Group by water body type and sum the lengths
        result = df.groupby(type_column)[length_column].sum().reset_index()
        
        # Step 6: Sort by total length in descending order
        result = result.sort_values(by=length_column, ascending=False)
        
        # Step 7: Format the results with two decimal places
        result[length_column] = result[length_column].round(2)
        
        return result
    
    except Exception as e:
        # Step 8: Handle errors during calculation
        print(f"An error occurred: {str(e)}")
        return None