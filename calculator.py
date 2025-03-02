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

def list_types():
    excel_file = "C:\\Users\\Ali Al Mahdi\\Desktop\\HTWD\\5 Semester\\Arbeit\\Gewässersteckbriefe mit kSt.xlsx"
    # excel_file = input("Enter your file path: ")
    # Load Excel data
    data = load_excel_data(excel_file)
    if data is None:
        return
    
    # Display available types
    print("\nAvailable Types:")
    for i, type_name in enumerate(data["Typ und Bezeichnung"], 1):
        print(f"{i}. {type_name}")
    
    # Get user type selection
    while True:
        try:
            type_index = int(input(f"\nSelect a type (1-{i}): ")) - 1
            if 0 <= type_index < len(data):
                break
            else:
                print(f"Please enter a number between 1 and {len(data)}")
        except ValueError:
            print("Please enter a valid number")

    # Get selected row
    selected_row = data.iloc[type_index]

    return selected_row
  
    
def main():
    
    selected_row = list_types()
    # Get min and max values
    slope_min = selected_row["Slope (min) in ‰"] / 1000  # Convert from ‰ to decimal
    slope_max = selected_row["Slope (max) in ‰"] / 1000  # Convert from ‰ to decimal
    strickler_min = selected_row["k_St (min)"]
    strickler_max = selected_row["k_St (max)"]
    
    # Calculate and display results
    print("\n*********************************")
    print(f"Selected Type: {selected_row['Typ und Bezeichnung']}")
    print(f"Flow: {selected_row['Strömung']}")
    print(f"Eco-region: {selected_row['Ökoregion']}")
    print(f"Substrate: {selected_row['Sohlsubstrat']}")
    print("*********************************")
    
    print("\n----- Min of Power input -----")
    w_eff_min = powerInput(slope_min, strickler_min)
    print(f"Slope (min): {slope_min:.6f}")
    print(f"Strickler (min): {strickler_min}")
    print(f"Result of power input min: {w_eff_min:.2f} w/m²")
    
    print("\n----- Max of Power input -----")
    w_eff_max = powerInput(slope_max, strickler_max)
    print(f"Slope (max): {slope_max:.6f}")
    print(f"Strickler (max): {strickler_max}")
    print(f"Result of power input max: {w_eff_max:.2f} w/m²")

if __name__ == "__main__":
    main()