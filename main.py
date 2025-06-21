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
    # 1. Hauptfunktion des Programms => Einstiegspunkt
    # Dateien laden
    data, result_df = load_all_files()
    if data is None or result_df is None:
        return

    # 2. Typen verarbeiten
    simulation_results_by_water_type = process_all_types(data, result_df)

    # Ergebnisse exportieren
    export_results(simulation_results_by_water_type, result_df)

    # 3. MyMicroplasticSim-Funktionen
    excel_file = "../Microplastic-River-Abrasion/calculation_results.xlsx"
    data = load_excel_data(excel_file)
    if data is None:
        return
    simulation_results_by_water_type = {}

    counter = 0
    plastic_em = plastic_emission()
    em_results = plastic_emission_per_river(data, plastic_em)

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
    
    # 5. total emission mass per river
    final_resulte = total_mp_mass_emission_per_river(simulation_results_by_water_type, em_results)
    # print(final_resulte)
    
    # 6. Ergebnisse in Excel speichern
    output_file = "finale_results.xlsx"
    save_results_to_excel(output_file, simulation_results_by_water_type ,final_resulte)
    print(f"Results saved in {output_file}\n")


if __name__ == "__main__":
    main()
