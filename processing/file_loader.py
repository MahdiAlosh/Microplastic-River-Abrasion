from my_water_analysis_sim.excel_io import load_excel_data, calculate_total_length_by_type

def load_all_files():
    try:
        data = load_excel_data("Gewässersteckbriefe mit kSt.xlsx")
        result_df = calculate_total_length_by_type("2025-02-28 Wasserkoerper Navigator 2022-2027  - Flusse.xlsx")
        return data, result_df
    except Exception as e:
        print(f"Fehler beim Laden der Dateien: {e}")
        return None, None
