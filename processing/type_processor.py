from my_water_analysis_sim.utils import extract_type_identifier, powerInput
from my_water_analysis_sim.calculator import polymerCalculator
import pandas as pd
from tabulate import tabulate

def process_all_types(data, result_df):
    all_results = []
    for i, type_name in enumerate(data["Typ und Bezeichnung"], 0):
        print(f"\n*********** {i+1}. {type_name} ***********")
        selected_row = data.iloc[i]
        result = process_single_type(type_name, selected_row, result_df)
        if result:
            all_results.append(result)
    return all_results

def process_single_type(type_name, selected_row, result_df):
    type_id = extract_type_identifier(type_name)
    if not type_id:
        print(f"Warning: Type Identifier für '{type_name}' nicht gefunden.")
        return None

    match = result_df[result_df["Gewässertyp"].apply(lambda x: extract_type_identifier(x) == type_id)]
    total_length = match.iloc[0]["Länge"] if not match.empty else 0

    slope_min = selected_row["Slope (min) in ‰"] / 1000
    slope_max = selected_row["Slope (max) in ‰"] / 1000
    strickler_min = selected_row["k_St (min)"]
    strickler_max = selected_row["k_St (max)"]

    w_eff_min = powerInput(slope_min, strickler_min)
    w_eff_max = powerInput(slope_max, strickler_max)

    polymer_min = polymerCalculator(w_eff_min)
    polymer_max = polymerCalculator(w_eff_max)

    polymer_min_len = {k: v * total_length for k, v in polymer_min.items()}
    polymer_max_len = {k: v * total_length for k, v in polymer_max.items()}

    print_type_tables(slope_min, slope_max, strickler_min, strickler_max, w_eff_min, w_eff_max, polymer_min, polymer_max, polymer_min_len, polymer_max_len)

    row = {
        "Type": type_name,
        "Length (km)": total_length,
        "Min Power (w/m²)": w_eff_min,
        "Max Power (w/m²)": w_eff_max,
    }
    for p in polymer_min:
        row[f"Min {p.upper()} (mg/m²*m)"] = polymer_min[p]
        row[f"Max {p.upper()} (mg/m²*m)"] = polymer_max[p]
        row[f"Min {p.upper()} To. Length (s) (mg/m²*m)"] = polymer_min_len[p]
        row[f"Max {p.upper()} To. Length (s) (mg/m²*m)"] = polymer_max_len[p]

    return row

def print_type_tables(slope_min, slope_max, strickler_min, strickler_max, w_min, w_max, p_min, p_max, p_min_len, p_max_len):
    print(tabulate([
        ["Parameter", "Minimum", "Maximum"],
        ["Slope", f"{slope_min:.6f}", f"{slope_max:.6f}"],
        ["Strickler", f"{strickler_min}", f"{strickler_max}"],
        ["Power Input (w/m²)", f"{w_min:.6f}", f"{w_max:.6f}"]
    ], headers="firstrow", tablefmt="grid"))

    table = [["Polymer", "Min Value (mg/m²*m)", "Max Value (mg/m²*m)", "Min Total (s)", "Max Total (s)"]]
    for p in p_min:
        table.append([
            p.upper(), f"{p_min[p]:.6f}", f"{p_max[p]:.6f}",
            f"{p_min_len[p]:.6f}", f"{p_max_len[p]:.6f}"
        ])
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
