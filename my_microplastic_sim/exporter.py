import os
import pandas as pd
from datetime import datetime
#from openpyxl import load_workbook
from PA.pa import pa
from PET.pet import pet
from PS.ps import ps

def save_results_to_excel(output_file, simulation_results_by_water_type, final_resulte):
    # Step 1: Prepare a list to collect simulation results for each polymer and water type
    data = []
    
    # Step 2: Load polymer dataframes for PA, PET, and PS
    pa_df,_,_= pa()
    pet_df,_,_ = pet()
    ps_df,_,_ = ps()

    # Step 3: Collect simulation results for each polymer and water type
    for water_type, polymers_data in simulation_results_by_water_type.items():
        for polymer, values in polymers_data.items():
            data.append({
                'Water Type': water_type,
                'Polymer': polymer,
                #'Final Diameter Min (m)': values['final_diameter_min'],
                #'Final Diameter Max (m)': values['final_diameter_max'],
                #'Total Diameter Loss Min (m)': values['total_loss_diameter_micro_min'],
                #'Total Diameter Loss Max (m)': values['total_loss_diameter_micro_max'],
                'Total Mass Loss micro Min (kg)': values['total_mass_loss_micro_min'],
                'Total Mass Loss micro Max (kg)': values['total_mass_loss_micro_max'],
                'Total Mass Loss macro Min (kg)': values['total_mass_loss_macro_min'],
                'Total Mass Loss macro Max (kg)': values['total_mass_loss_macro_max'],
                #'Total Volume Loss micro Min (m³)': values['total_volume_loss_micro_min'],
                #'Total Volume Loss micro Max (m³)': values['total_volume_loss_micro_max'],
                #'Total Volume Loss macro Min (m³)': values['total_volume_loss_macro_min'],
                #'Total Volume Loss macro Max (m³)': values['total_volume_loss_macro_max'],
                'Remaining time Min Micro': values['remaining_h_min_micro'],
                'Remaining time Max Micro': values['remaining_h_max_micro'],
                'Remaining time Min Macro': values['remaining_h_min_macro'],
                'Remaining time Max Macro': values['remaining_h_max_macro'],
            })
    
    # Step 4: Convert the final emission results to a DataFrame
    final_resulte_data = []
    for water_type, values in final_resulte.items():
        for polymer, polymer_values in values.items():
            final_resulte_data.append({
                'Water Type': water_type,
                'Polymer': polymer,
                'Total MP production macro min (kg)': polymer_values["total_mass_loss_min_macro"],
                'Total MP production micro min (kg)': polymer_values["total_mass_loss_min_micro"],
                'Total MP production macro max (kg)': polymer_values["total_mass_loss_max_macro"],
                'Total MP production micro max (kg)': polymer_values["total_mass_loss_max_micro"]
            })

    try:
        # Step 5: Create DataFrames from the collected data
        df = pd.DataFrame(data)
        final_resulte_df = pd.DataFrame(final_resulte_data)
        if os.path.exists(output_file):
            # Step 6: If the file exists, append or replace the sheets
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name='Polymer_Sim_Results', index=False)
                    final_resulte_df.to_excel(writer, sheet_name='MP_production_Results', index=False)
                    pa_df.to_excel(writer, sheet_name="PA", index=False)
                    pet_df.to_excel(writer, sheet_name="PET", index=False)
                    ps_df.to_excel(writer, sheet_name="PS", index=False)
        else:
            # Step 7: If the file doesn't exist, create it and write all sheets
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Polymer_Sim_Results', index=False)
                final_resulte_df.to_excel(writer, sheet_name='MP_production_Results', index=False)
                pa_df.to_excel(writer, sheet_name="PA", index=False)
                pet_df.to_excel(writer, sheet_name="PET", index=False)
                ps_df.to_excel(writer, sheet_name="PS", index=False)

    except Exception as e:
        # Step 8: Print an error message if saving fails
        print(f"Error saving results to Excel: {e}")

