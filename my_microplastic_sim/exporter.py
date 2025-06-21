import os
import pandas as pd
#from openpyxl import load_workbook
from PA.pa import pa
from PET.pet import pet
from PS.ps import ps

def save_results_to_excel(output_file, simulation_results_by_water_type, final_resulte):
    data = []
    
    pa_df,_,_= pa()
    pet_df,_,_ = pet()
    ps_df,_,_ = ps()

    for water_type, polymers_data in simulation_results_by_water_type.items():
        for polymer, values in polymers_data.items():
            data.append({
                'Water Type': water_type,
                'Polymer': polymer,
                'Final Diameter Min (m)': values['final_diameter_min'],
                'Final Diameter Max (m)': values['final_diameter_max'],
                'Total Diameter Loss Min (m)': values['total_loss_diameter_min'],
                'Total Diameter Loss Max (m)': values['total_loss_diameter_max'],
                'Total Mass Loss Min (kg)': values['total_mass_loss_min'],
                'Total Mass Loss Max (kg)': values['total_mass_loss_max'],
                'Total Volume Loss Min (m³)': values['total_volume_loss_min'],
                'Total Volume Loss Max (m³)': values['total_volume_loss_max'],
                'Remaining Km Min': values['remaining_km_min'],
                'Remaining Km Max': values['remaining_km_max']
            })
    
    # Convert final_resulte to DataFrame
    final_resulte_data = []
    for water_type, values in final_resulte.items():
        for polymer, polymer_values in values.items():
            final_resulte_data.append({
                'Water Type': water_type,
                'Polymer': polymer,
                'Total mass emission min macro(kg)': polymer_values["total_mass_loss_min_macro"],
                'Total mass emission min micro(kg)': polymer_values["total_mass_loss_min_micro"],
                'Total mass emission max macro(kg)': polymer_values["total_mass_loss_max_macro"],
                'Total mass emission max micro(kg)': polymer_values["total_mass_loss_max_micro"]
            })

    try:
        df = pd.DataFrame(data)
        final_resulte_df = pd.DataFrame(final_resulte_data)
        if os.path.exists(output_file):
            # File exists: append/replace sheets
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name='Polymer_Sim_Results', index=False)
                    final_resulte_df.to_excel(writer, sheet_name='Final_Results', index=False)
                    pa_df.to_excel(writer, sheet_name="PA", index=False)
                    pet_df.to_excel(writer, sheet_name="PET", index=False)
                    ps_df.to_excel(writer, sheet_name="PS", index=False)
        else:
            # File doesn't exist: create and write all sheets
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Polymer_Sim_Results', index=False)
                final_resulte_df.to_excel(writer, sheet_name='Final_Results', index=False)
                pa_df.to_excel(writer, sheet_name="PA", index=False)
                pet_df.to_excel(writer, sheet_name="PET", index=False)
                ps_df.to_excel(writer, sheet_name="PS", index=False)

    except Exception as e:
        print(f"Error saving results to Excel: {e}")

