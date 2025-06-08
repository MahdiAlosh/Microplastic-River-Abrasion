import pandas as pd
#from openpyxl import load_workbook
from PA.pa import pa
from PET.pet import pet
from PS.ps import ps

def save_results_to_excel(input_file, output_file, all_results):
    data = []
    
    pa_df = pa()
    pet_df = pet()
    ps_df = ps()

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
    try:
        df = pd.DataFrame(data)
        if input_file == output_file:
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name='Polymer_Results', index=False)
                pa_df.to_excel(writer, sheet_name="PA", index=False)
                pet_df.to_excel(writer, sheet_name="PET", index=False)
                ps_df.to_excel(writer, sheet_name="PS", index=False)
        else:
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, sheet_name='Polymer_Results', index=False)
                pa_df.to_excel(writer, sheet_name="PA", index=False)
                pet_df.to_excel(writer, sheet_name="PET", index=False)
                ps_df.to_excel(writer, sheet_name="PS", index=False)

    except Exception as e:
        print(f"Error saving results to Excel: {e}")

