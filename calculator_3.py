import math as m
import pandas as pd
import os.path
from tabulate import tabulate

def powerInput(slope, strickler):
    p = 980   # density in kg/m³
    g = 9.81  # acceleration in m/s²
    h = 1.53  # hight of water column in m
    e = 0.1   # coefficient of efficiency
    r = h     # hydraulic radius ^2/3

    i = slope     # slope from Excel sheet converted to decimal number
    k = strickler # strickler coefficient from Excel sheet

    result = (p * g * h * i) * (k * m.pow(r, 2/3) * m.pow(i, 1/2)) * e 
    
    return result

def polymerCalcutator(w_eff):
    """
    Multiply the power input value with each polymer coefficient and return results.
    Args:
        w_eff (float): Power input value in w/m²
    Returns:
        dict: Dictionary with polymer names as keys and calculated values as values
    """
    polymer = {
        "ps_tio": 1.00036,
        "ps": 0.42826,
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
  
def main():
    excel_file = "C:\\Users\\Ali Al Mahdi\\Desktop\\HTWD\\5 Semester\\Arbeit\\Gewässersteckbriefe mit kSt.xlsx"
    # excel_file = input("Enter your file path: ")
    # Load Excel data
    data = load_excel_data(excel_file)
    if data is None:
        return
    
    # Create a list to hold all results for the final table
    all_results = []
    
    # Process each type
    for i, type_name in enumerate(data["Typ und Bezeichnung"], 0):
        print(f"\n*********** {i+1}. {type_name} ***********")
        selected_row = data.iloc[i]
    
        # Get min and max values
        slope_min = selected_row["Slope (min) in ‰"] / 1000  # Convert from ‰ to decimal
        slope_max = selected_row["Slope (max) in ‰"] / 1000  # Convert from ‰ to decimal
        strickler_min = selected_row["k_St (min)"]
        strickler_max = selected_row["k_St (max)"]
        
        # Calculate min values
        w_eff_min = powerInput(slope_min, strickler_min)
        relative_polymer_min = polymerCalcutator(w_eff_min)
        
        # Calculate max values
        w_eff_max = powerInput(slope_max, strickler_max)
        relative_polymer_max = polymerCalcutator(w_eff_max)
        
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
        polymer_table = [["Polymer", "Min Value (mg/m²*m)", "Max Value (mg/m²*m)"]]
        for polymer in relative_polymer_min.keys():
            polymer_table.append([
                polymer.upper(), 
                f"{relative_polymer_min[polymer]:.6f}", 
                f"{relative_polymer_max[polymer]:.6f}"
            ])
        print(tabulate(polymer_table, headers="firstrow", tablefmt="grid"))
        
        # Store results for summary table
        result_row = {
            #"Type": f"{i+1}. {type_name}",
            "Type": type_name,
            "Min Power": w_eff_min,
            "Max Power": w_eff_max
        }
        
        # Add polymer values to the result row
        for polymer in relative_polymer_min.keys():
            result_row[f"Min {polymer.upper()}"] = relative_polymer_min[polymer]
            result_row[f"Max {polymer.upper()}"] = relative_polymer_max[polymer]
            
        all_results.append(result_row)
    
    # Create a DataFrame
    df_results = pd.DataFrame(all_results)
    
    # Format numeric columns
    numeric_cols = df_results.columns.drop('Type')
    for col in numeric_cols:
        df_results[col] = df_results[col].map('{:.6f}'.format)
    
    # # Print the summary table
    # print(tabulate(df_results, headers='keys', tablefmt='grid', showindex=False))
    
    # Export to Excel
    output_file = "calculation_results.xlsx"
    df_results.to_excel(output_file, index=False)
    print(f"\nResults exported to {output_file}")

if __name__ == "__main__":
    main()