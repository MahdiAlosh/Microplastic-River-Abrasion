from processing.file_loader import load_all_files
from processing.type_processor import process_all_types
from processing.output_formatter import export_results # print_total_lengths
from my_microplastic_sim.loader import load_excel_data
from my_microplastic_sim.simulator import t6_simulate_abrasion
from my_microplastic_sim.exporter import save_results_to_excel
from Emission_sim.plastic_emission import plastic_emission
from Emission_sim.plastic_em_per_river import plastic_emission_per_river
from Emission_sim.total_mp_mass_emission_per_river import total_mp_mass_emission_per_river

def main():
    # Main function of the program - entry point
    # Step 1: Load all necessary files and data
    data, result_df = load_all_files()
    if data is None or result_df is None:
        return

    # Step 2: Process all water types using the loaded data
    simulation_results_by_water_type = process_all_types(data, result_df)

    # Step 3: Export the processed results (e.g., to Excel or other formats)
    export_results(simulation_results_by_water_type, result_df)

    # Step 4: Load calculation results from an Excel file for further simulation
    excel_file = "../Microplastic-River-Abrasion/calculation_results.xlsx"
    data = load_excel_data(excel_file)
    if data is None:
        return
    simulation_results_by_water_type = {}

    # Step 5: Calculate plastic emission and emission per river
    counter = 0
    plastic_em = plastic_emission()
    em_results = plastic_emission_per_river(data, plastic_em)

    # Step 6: Simulate abrasion for each water type and store the results
    for _, row in data.iterrows():
        water_type = row["Type"]
        total_length = row["Length (km)"]
        w_eff_min = row["Min Power (w/m²)"]
        w_eff_max = row["Max Power (w/m²)"]
        if total_length > 0:
            counter += 1
            abrasion_simulation_results = t6_simulate_abrasion(total_length, w_eff_min, w_eff_max)
            simulation_results_by_water_type[water_type] = abrasion_simulation_results
    
    print(f"Simulation completed for {counter} water types.\n")
    
    # Step 7: Calculate the total microplastic emission mass per river
    final_resulte = total_mp_mass_emission_per_river(simulation_results_by_water_type, em_results)
    # print(final_resulte)
    
    # Step 8: Save the final results to an Excel file
    output_file = "finale_results.xlsx"
    save_results_to_excel(output_file, simulation_results_by_water_type ,final_resulte)
    print(f"Results saved in {output_file}\n")


if __name__ == "__main__":
    main()
