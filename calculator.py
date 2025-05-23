import math as m
import pandas as pd
import os.path
from tabulate import tabulate
import re  # Regular expressions for extracting type numbers

def extract_type_identifier(type_name):
    """
    Extract the type number (and optional suffix) from a type name string.
    Example: "Typ 10: Kiesgeprägte Ströme" -> 10
             "Typ: 15_g" -> 15_g
    """
    match = re.search(r"Typ\s*(\d+(\.\d+)?(_[A-Za-z]+)?)|\(Typ:\s*(\d+(\.\d+)?(_[A-Za-z]+)?)\)", type_name)
    if match:
        # Return the matched group (either from "Typ <number>" or "(Typ: <number>)") and normalize to lowercase
        return (match.group(1) or match.group(4)).lower()
    return None

def powerInput(slope, strickler):
    p = 980   # density in kg/m³
    g = 9.81  # acceleration in m/s²
    h = 1.53  # height of water column in m
    e = 0.1   # coefficient of efficiency
    r = h     # hydraulic radius ^2/3

    i = slope     # slope from Excel sheet converted to decimal number
    k = strickler # strickler coefficient from Excel sheet

    result = (p * g * h * i) * (k * m.pow(r, 2/3) * m.pow(i, 1/2)) * e 
    
    return result

def polymerCalculator(w_eff):
    """
    Multiply the power input value with each polymer coefficient and return results.
    Args:
        w_eff (float): Power input value in w/m²
    Returns:
        dict: Dictionary with polymer names as keys and calculated values as values
    """
    polymer = {
        "ps_tio": 1.00036,
        "ps": 0.81021,
        "petg": 0.52683,
        "pet": 0.35373,
        "pa6": 0.32447
        }
    
    # Calculate the result for each polymer by multiplying w_eff with the polymer coefficient
    result = {}
    for name, coefficient in polymer.items():
        result[name] = w_eff * coefficient
    
    return result

def load_excel_data(file_path):
    """Load data from Excel file and return as DataFrame"""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found!")
        return None
    try:
        # Read Excel file
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
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
        # Read the Excel file
        df = pd.read_excel(excel_file_path)
        
        df = df.iloc[:-2]

        # Ensure the required columns exist
        if length_column not in df.columns or type_column not in df.columns:
            raise ValueError(f"Required columns '{length_column}' or '{type_column}' not found in the Excel file.")
        
        # Convert length values to numeric, handling potential formatting issues
        df[length_column] = pd.to_numeric(df[length_column], errors='coerce')
        
        # Group by water body type and sum the lengths
        result = df.groupby(type_column)[length_column].sum().reset_index()
        
        # Sort by total length in descending order
        result = result.sort_values(by=length_column, ascending=False)
        
        # Format the results with two decimal places
        result[length_column] = result[length_column].round(2)
        
        return result
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
  
def main():
    # excel_file = "C:\\Users\\Ali Al Mahdi\\Desktop\\HTWD\\5 Semester\\Arbeit\\Gewässersteckbriefe mit kSt.xlsx"
    excel_file = input("Enter your file path (Gewässersteckbriefe): ")
    data = load_excel_data(excel_file)
    if data is None:
        return
    
    # excel_file_length = "C:\\Users\\Ali Al Mahdi\\Desktop\\HTWD\\5 Semester\\Arbeit\\2025-02-28 Wasserkoerper Navigator 2022-2027 - Flüsse.xlsx"
    excel_file_length = input("Enter your file path (2025-02-28 Wasserkoerper): ")
    result_df = calculate_total_length_by_type(excel_file_length)
    if result_df is None:
        return
    
    # ======================================
    print("\nTotal Length by Water Body Type:")
    print("================================")
    for index, row in result_df.iterrows():
            water_type = row["Gewässertyp"]
            total_length = row["Länge"]
            print(f"{water_type}: {total_length} km")
            

    print(f"\nTotal Length of All Water Bodies: {result_df['Länge'].sum():.2f} km")
    # ======================================

    # Create a list to hold all results for the final table
    all_results = []
    
    # Process each type
    for i, type_name in enumerate(data["Typ und Bezeichnung"], 0):
        print(f"\n*********** {i+1}. {type_name} ***********")
        selected_row = data.iloc[i]

        # Extract the type identifier from the current type name
        type_identifier_data = extract_type_identifier(type_name)
        if type_identifier_data is None:
            # If no identifier is found, print a warning and skip this iteration
            print(f"Warning: Could not extract type number from '{type_name}'. Skipping calculations.")
            continue
        
        # Find matching rows in result_df where the type identifier matches
        matching_rows = result_df[result_df["Gewässertyp"].apply(lambda x: extract_type_identifier(x) == type_identifier_data)]
        
        # Select the matching row and extract the total length
        if matching_rows.empty:
            # If no matching rows are found, print a warning and set total length to 0
            print(f"Warning: No total length found for type '{type_name}' (Type {type_identifier_data}). Setting length-dependent values to 0.")
            total_length = 0
        else:
            # If matching rows are found, extract the total length from the first matching row
            total_length = matching_rows.iloc[0]["Länge"]

        # Get min and max values
        slope_min = selected_row["Slope (min) in ‰"] / 1000  # Convert from ‰ to decimal
        slope_max = selected_row["Slope (max) in ‰"] / 1000  # Convert from ‰ to decimal
        strickler_min = selected_row["k_St (min)"]
        strickler_max = selected_row["k_St (max)"]
        
        # Calculate min values
        w_eff_min = powerInput(slope_min, strickler_min)
        relative_polymer_min = polymerCalculator(w_eff_min)
        
        # Calculate max values
        w_eff_max = powerInput(slope_max, strickler_max)
        relative_polymer_max = polymerCalculator(w_eff_max)
        
        # Calculate min and max values multiplied by total length
        relative_polymer_min_with_length = {k: v * total_length for k, v in relative_polymer_min.items()}
        relative_polymer_max_with_length = {k: v * total_length for k, v in relative_polymer_max.items()}
        
        # Print detailed results for each type
        print("\nDetailed Results:")
        
        # Create a table for min and max parameters
        params_table = [
            ["Parameter", "Minimum", "Maximum"],
            ["Slope", f"{slope_min:.6f}", f"{slope_max:.6f}"],
            ["Strickler", f"{strickler_min}", f"{strickler_max}"],
            ["Power Input (w/m²)", f"{w_eff_min:.6f}", f"{w_eff_max:.6f}"]
        ]
        print(tabulate(params_table, headers="firstrow", tablefmt="grid"))
        
        # Create a table for polymer results
        polymer_table = [
            ["Polymer", "Min Value (mg/m²*m)", "Max Value (mg/m²*m)", "Min Value (s)", "Max Value (s)"]
        ]
        for polymer in relative_polymer_min.keys():
            polymer_table.append([
                polymer.upper(), 
                f"{relative_polymer_min[polymer]:.6f}", 
                f"{relative_polymer_max[polymer]:.6f}",
                f"{relative_polymer_min_with_length[polymer]:.6f}",
                f"{relative_polymer_max_with_length[polymer]:.6f}"
            ])
        print(tabulate(polymer_table, headers="firstrow", tablefmt="grid"))
        
        # Store results for summary table
        result_row = {
            "Type": type_name,
            "Length (km)": total_length,
            "Min Power (w/m²)": w_eff_min,
            "Max Power (w/m²)": w_eff_max
        }
        
        # Add polymer values to the result row
        for polymer in relative_polymer_min.keys():
            result_row[f"Min {polymer.upper()} (mg/m²*m)"] = relative_polymer_min[polymer]
            result_row[f"Max {polymer.upper()} (mg/m²*m)"] = relative_polymer_max[polymer]
            result_row[f"Min {polymer.upper()} To. Length (s) (mg/m²*m)"] = relative_polymer_min_with_length[polymer]
            result_row[f"Max {polymer.upper()} To. Length (s) (mg/m²*m)"] = relative_polymer_max_with_length[polymer]
    
        all_results.append(result_row)

    # Create a DataFrame
    df_results = pd.DataFrame(all_results)
    
    # Format numeric columns
    numeric_cols = df_results.columns.drop('Type')

    for col in numeric_cols:
        if col == "Length (km)":  # Special formatting for the "Länge" column
            df_results[col] = df_results[col].map('{:.2f}'.format)
        else:
            df_results[col] = df_results[col].map('{:.6f}'.format)

    # Add a new row for "total_length_all_rivers"
    new_row = {"Type": "Gesamte Länge aller Flüsse", "Length (km)": result_df['Länge'].sum()}
    # Fill other columns with empty values
    for col in numeric_cols:
        if col != "Length (km)":
            new_row[col] = " "  # empty string
    # Append the new row to the DataFrame
    all_results.append(new_row)

    df_results = pd.DataFrame(all_results)

    # Export to Excel
    output_file = "calculation_results.xlsx"
    df_results.to_excel(output_file, index=False)
    print(f"\nResults exported to {output_file}\n")

if __name__ == "__main__":
    main()