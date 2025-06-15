from processing.file_loader import load_all_files
from processing.type_processor import process_all_types
from processing.output_formatter import export_results # print_total_lengths
from my_microplastic_sim.loader import load_excel_data
from my_microplastic_sim.simulator import simulate_abrasion
from my_microplastic_sim.exporter import save_results_to_excel
from Emission_sim.plastic_emission import plastic_emission

def main():
    # 1. Hauptfunktion des Programms => Einstiegspunkt
    # Dateien laden
    data, result_df = load_all_files()
    if data is None or result_df is None:
        return

    # Gesamtlängen ausgeben
    # print_total_lengths(result_df)

    # Typen verarbeiten
    all_results = process_all_types(data, result_df)

    # Ergebnisse exportieren
    export_results(all_results, result_df)

    #2. MyMicroplasticSim-Funktionen
    excel_file = "../Microplastic-River-Abrasion/calculation_results.xlsx"
    data = load_excel_data(excel_file)
    if data is None:
        return
    all_results = {}
    counter = 0
    for _, row in data.iterrows():
        water_type = row["Type"]
        total_length = row["Length (km)"]
        w_eff_min = row["Min Power (w/m²)"]
        w_eff_max = row["Max Power (w/m²)"]
        if total_length > 0:
            counter += 1
            results = simulate_abrasion(total_length, w_eff_min, w_eff_max)
            all_results[water_type] = results

    save_results_to_excel("finale_results.xlsx", all_results)
    print("Results saved in finale_results.xlsx\n")
    print(f"Simulation completed for {counter} water types.\n")
    
    # 3. Emission_sim-Funktionen
    plastic_emission()

if __name__ == "__main__":
    main()
