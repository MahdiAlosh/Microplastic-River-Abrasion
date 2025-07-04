from my_water_analysis_sim.utils import extract_type_identifier, powerInput
from my_water_analysis_sim.length_calculator import polymerCalculator
import pandas as pd
# from tabulate import tabulate

def process_all_types(data, result_df):
    # Step 1: Initialize a list to collect results for all water types
    all_results = []
    # Step 2: Iterate over each water type in the input data
    for i, type_name in enumerate(data["Typ und Bezeichnung"], 0):
        # Step 2a: Select the corresponding row for the current water type
        selected_row = data.iloc[i]
        # Step 2b: Process the current water type and get the result
        result = process_single_type(type_name, selected_row, result_df)
        # Step 2c: If a result is returned, add it to the results list
        if result:
            all_results.append(result)
    # Step 3: Return the list of results for all water types
    return all_results

def process_single_type(type_name, selected_row, result_df):
    # Step 1: Extract the type identifier from the type name
    type_id = extract_type_identifier(type_name)
    if not type_id:
        # print(f"Warning: Type Identifier für '{type_name}' nicht gefunden.")
        # Step 1a: If no identifier is found, skip this type
        return None

    # Step 2: Find the matching row in the result DataFrame for this type
    match = result_df[result_df["Gewässertyp"].apply(lambda x: extract_type_identifier(x) == type_id)]
    total_length = match.iloc[0]["Länge"] if not match.empty else 0

    # Step 3: Extract slope and Strickler values for min and max scenarios and water levels
    slope_min = selected_row["Slope (min) in ‰"] / 1000
    slope_max = selected_row["Slope (max) in ‰"] / 1000
    strickler_min = selected_row["k_St (min)"]
    strickler_max = selected_row["k_St (max)"]
    water_level = selected_row["Water level in m"]

    # Step 4: Calculate the power input for min and max scenarios
    w_eff_min = powerInput(slope_min, strickler_min, water_level)
    w_eff_max = powerInput(slope_max, strickler_max, water_level)

    # Step 5: Calculate abrasion for each polymer for min and max scenarios
    polymer_min = polymerCalculator(w_eff_min)
    polymer_max = polymerCalculator(w_eff_max)

    # Step 6: Multiply abrasion by total length for each polymer
    polymer_min_len = {k: v * total_length for k, v in polymer_min.items()}
    polymer_max_len = {k: v * total_length for k, v in polymer_max.items()}

    # print_type_tables(slope_min, slope_max, strickler_min, strickler_max, w_eff_min, w_eff_max, polymer_min, polymer_max, polymer_min_len, polymer_max_len)

    #calculate exposure time
    #flow_velocity = water_level ** (2/3) * slope_max

    # exposure_time_min = ((total_length*1000) / (strickler_min * (water_level ** (2/3)) * ((slope_min) ** (1/2)))) / 3600
    # exposure_time_max = ((total_length*1000) / (strickler_max * (water_level ** (2/3)) * ((slope_max) ** (1/2)))) / 3600
    
    if total_length == 0 or strickler_min == 0 or water_level == 0 or slope_min == 0:
        exposure_time_min = 0
        # print(f"Warning: Exposure time for '{type_name}' is NaN, Strickler: {strickler_min}, Water level: {water_level}, Slope: {slope_min}")
    else:
        exposure_time_min = ((total_length*1000) / (strickler_min * (water_level ** (2/3)) * ((slope_min) ** (1/2)))) / 3600

    if total_length == 0 or strickler_max == 0 or water_level == 0 or slope_max == 0:
        exposure_time_max = 0
        # print(f"Warning: Exposure time for '{type_name}' is NaN, Strickler: {strickler_max}, Water level: {water_level}, Slope: {slope_max}")
    else:
        exposure_time_max = ((total_length*1000) / (strickler_max * (water_level ** (2/3)) * ((slope_max) ** (1/2)))) / 3600
    

    # Step 7: Build the result row for this water type
    row = {
        "Type": type_name,
        "Length (km)": total_length,
        "Water level (m)": water_level,
        "Min exposure time (h)": exposure_time_min, #calculates exposure time in h
        "Max exposure time (h)": exposure_time_max, #calculates exposure time in h
        "Min Power (w/m²)": w_eff_min,
        "Max Power (w/m²)": w_eff_max,
        
    }
    for p in polymer_min:
        row[f"Min {p.upper()} (mg/m²*m)"] = polymer_min[p]
        row[f"Max {p.upper()} (mg/m²*m)"] = polymer_max[p]
        row[f"Min {p.upper()} To. Length (s) (mg/m²*m)"] = polymer_min_len[p]
        row[f"Max {p.upper()} To. Length (s) (mg/m²*m)"] = polymer_max_len[p]


    # Step 8: Return the result row
    return row

# def print_type_tables(slope_min, slope_max, strickler_min, strickler_max, w_min, w_max, p_min, p_max, p_min_len, p_max_len):
#     print(tabulate([
#         ["Parameter", "Minimum", "Maximum"],
#         ["Slope", f"{slope_min:.6f}", f"{slope_max:.6f}"],
#         ["Strickler", f"{strickler_min}", f"{strickler_max}"],
#         ["Power Input (w/m²)", f"{w_min:.6f}", f"{w_max:.6f}"]
#     ], headers="firstrow", tablefmt="grid"))

#     table = [["Polymer", "Min Value (mg/m²*m)", "Max Value (mg/m²*m)", "Min Total (s)", "Max Total (s)"]]
#     for p in p_min:
#         table.append([
#             p.upper(), f"{p_min[p]:.6f}", f"{p_max[p]:.6f}",
#             f"{p_min_len[p]:.6f}", f"{p_max_len[p]:.6f}"
#         ])
#     print(tabulate(table, headers="firstrow", tablefmt="grid"))
