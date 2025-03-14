import math as m
import pandas as pd
import os.path

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
    
    # Display types
    for i, type_name in enumerate(data["Typ und Bezeichnung"], 0):
        print("\n*******************************")
        print(f"{i+1}. {type_name}")
        selected_row = data.iloc[i]
    
        # Get min and max values
        slope_min = selected_row["Slope (min) in ‰"] / 1000  # Convert from ‰ to decimal
        slope_max = selected_row["Slope (max) in ‰"] / 1000  # Convert from ‰ to decimal
        strickler_min = selected_row["k_St (min)"]
        strickler_max = selected_row["k_St (max)"]
        
        print("----- Min of Power input -----")
        w_eff_min = powerInput(slope_min, strickler_min)
        relative_polymer_min = polymerCalcutator(w_eff_min)
        print(f"Slope (min): {slope_min:.6f}")
        print(f"Strickler (min): {strickler_min}")
        print(f"Result of power input min: {w_eff_min:.6f} w/m²")
        print("\n----- Polymer Results (Min) -----")
        for polymer, value in relative_polymer_min.items():
            print(f"{polymer.upper()}: {value:.6f} mg/m²*m")
        
        print("\n----- Max of Power input -----")
        w_eff_max = powerInput(slope_max, strickler_max)
        relative_polymer_max = polymerCalcutator(w_eff_max)
        print(f"Slope (max): {slope_max:.6f}")
        print(f"Strickler (max): {strickler_max}")
        print(f"Result of power input max: {w_eff_max:.6f} w/m²")
        print("\n----- Polymer Results (Max) -----")
        for polymer, value in relative_polymer_max.items():
            print(f"{polymer.upper()}: {value:.6f} mg/m²*m")
        
    print("*******************************")
    print()

#TODO: Do Task 2 for every Type underneth 

if __name__ == "__main__":
    main()