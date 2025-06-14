import os
import pandas as pd
#from openpyxl import load_workbook
from PA.pa import pa
from PET.pet import pet
from PS.ps import ps
from processing.em_factor import calculate_emission_factors

def save_results_to_excel(output_file, all_results):
    data = []
    
    pa_df,_,_= pa()
    pet_df,_,_ = pet()
    ps_df,_,_ = ps()

    # Calculate emission factors
    emission_factors,_,_ = calculate_emission_factors()
    emission = []

    for water_type, polymers_data in all_results.items():
        for polymer, values in polymers_data.items():
            data.append({
                'Water Type': water_type,
                'Polymer': polymer,
                'Final Diameter Min (µm)': values['final_diameter_min'],
                'Final Diameter Max (µm)': values['final_diameter_max'],
                'Total Diameter Loss Min (µm)': values['total_loss_diameter_min'],
                'Total Diameter Loss Max (µm)': values['total_loss_diameter_max'],
                'Total Mass Loss Min (mg)': values['total_mass_loss_min'],
                'Total Mass Loss Max (mg)': values['total_mass_loss_max'],
                'Total Volume Loss Min (µm³)': values['total_volume_loss_min'],
                'Total Volume Loss Max (µm³)': values['total_volume_loss_max'],
                'Remaining Km Min': values['remaining_km_min'],
                'Remaining Km Max': values['remaining_km_max']
            })
    for district, factor in emission_factors.items():
        emission.append({
            'District': district,
            'Emission Factor': factor
        })

    try:
        df = pd.DataFrame(data)
        emission_df = pd.DataFrame(emission)
        if os.path.exists(output_file):
            # File exists: append/replace sheets
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name='Polymer_Results', index=False)
                    pa_df.to_excel(writer, sheet_name="PA", index=False)
                    pet_df.to_excel(writer, sheet_name="PET", index=False)
                    ps_df.to_excel(writer, sheet_name="PS", index=False)
                    emission_df.to_excel(writer, sheet_name="Emission_Factors", index=False)
        else:
            # File doesn't exist: create and write all sheets
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Polymer_Results', index=False)
                pa_df.to_excel(writer, sheet_name="PA", index=False)
                pet_df.to_excel(writer, sheet_name="PET", index=False)
                ps_df.to_excel(writer, sheet_name="PS", index=False)
                emission_df.to_excel(writer, sheet_name="Emission_Factors", index=False)

    except Exception as e:
        print(f"Error saving results to Excel: {e}")

