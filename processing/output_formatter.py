import pandas as pd
import os
from datetime import datetime

def export_results(all_results, result_df):
    # Step 1: Convert the results to a DataFrame
    df = pd.DataFrame(all_results)
    numeric_cols = df.columns.drop("Type")

    # Step 2: Format numeric columns for better readability
    for col in numeric_cols:
        if col == "Length (km)":
            df[col] = df[col].map("{:.2f}".format)
        else:
            df[col] = df[col].map("{:.6f}".format)

    # Step 3: Add a summary row for the total river length
    new_row = {"Type": "Total length of all rivers", "Length (km)": result_df["Länge"].sum()}
    for col in numeric_cols:
        if col != "Length (km)":
            new_row[col] = " "

    all_results.append(new_row)
    df = pd.DataFrame(all_results)
    # new_df = pd.DataFrame([new_row])
    # df = pd.concat([df, new_df], ignore_index=True)

    # Step 4: Export the DataFrame to an Excel file
    # Go one directory up from the current file's directory
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_folder = "simulation_results"
    results_path = os.path.join(parent_dir, results_folder)
    # Step 5: Create the folder if it doesn't exist
    os.makedirs(results_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M")
    filename = f"calculation_results_{timestamp}.xlsx"
    output_file = os.path.join(results_path, filename)
    
    df.to_excel(output_file, index=False)
    print(f"\nResults exported to {output_file}\n")
