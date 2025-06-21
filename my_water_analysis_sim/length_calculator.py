import pandas as pd

def polymerCalculator(w_eff):
    """
    Multiply the power input value with each polymer coefficient and return results.
    Args:
        w_eff (float): Power input value in w/m²
    Returns:
        dict: Dictionary with polymer names as keys and calculated values as values
    """
    # Step 1: Define the abrasion coefficients for each polymer
    polymer = {
        "ps": 0.81021,
        "pet": 0.35373,
        "pa": 0.32447
        }
    
    # Step 2: Calculate the result for each polymer by multiplying w_eff with the polymer coefficient
    result = {}
    for name, coefficient in polymer.items():
        result[name] = w_eff * coefficient
    
    # Step 3: Return the calculated results as a dictionary
    return result

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








