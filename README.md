# Microplastic River Abrasion

This project analyzes microplastic abrasion in river environments using experimental Excel data. It is intended to simulate and evaluate how microplastics may form and disperse based on physical and chemical properties of polymers, abrasion parameters, and river characteristics.

---

## Project Structure

```
Microplastic-River-Abrasion/
├── 2025-02-28 Wasserkoerper Navigator 2022-2027  - Flusse.xlsx
├── Gewässersteckbriefe mit kSt.xlsx
├── PA
│   ├── pa.py
│   └── scr
│       ├── __init__.py
│       ├── macro.py
│       ├── micro.py
│       ├── pa_summary_df.py
│       ├── sinks_EU_Clothing (product sector)_PA_Surface water (macro).csv
│       ├── sinks_EU_Clothing (product sector)_PA_Surface water (micro).csv
│       ├── sinks_EU_Domestic primary plastic production_PA_Surface water (micro).csv
│       ├── sinks_EU_Household textiles (product sector)_PA_Surface water (macro).csv
│       ├── sinks_EU_Household textiles (product sector)_PA_Surface water (micro).csv
│       ├── sinks_EU_Import of primary plastics_PA_Surface water (micro).csv
│       ├── sinks_EU_Intentionally produced microparticles_PA_Surface water (micro).csv
│       └── sinks_EU_Technical textiles_PA_Surface water (macro).csv
├── PET
│   ├── pet.py
│   └── scr
│       ├── __init__.py
│       ├── macro.py
│       ├── micro.py
│       ├── pet_summary_df.py
│       ├── sinks_EU_Clothing (product sector)_PET_Surface water (macro).csv
│       ├── sinks_EU_Clothing (product sector)_PET_Surface water (micro).csv
│       ├── sinks_EU_Domestic primary plastic production_PET_Surface water (micro).csv
│       ├── sinks_EU_Household textiles (product sector)_PET_Surface water (macro).csv
│       ├── sinks_EU_Household textiles (product sector)_PET_Surface water (micro).csv
│       ├── sinks_EU_Import of primary plastics_PET_Surface water (micro).csv
│       ├── sinks_EU_Intentionally produced microparticles_PET_Surface water (micro).csv
│       ├── sinks_EU_Packaging_PET_Surface water (macro).csv
│       ├── sinks_EU_Packaging_PET_Surface water (micro).csv
│       ├── sinks_EU_Technical textiles_PET_Surface water (macro).csv
│       └── sinks_EU_Technical textiles_PET_Surface water (micro).csv
├── PS
│   ├── ps.py
│   └── scr
│       ├── __init__.py
│       ├── macro.py
│       ├── micro.py
│       ├── ps_summary_df.py
│       ├── sinks_EU_Agriculture_PS_Surface water (macro).csv
│       ├── sinks_EU_Agriculture_PS_Surface water (micro).csv
│       ├── sinks_EU_Domestic primary plastic production_PS_Surface water (micro).csv
│       ├── sinks_EU_Import of primary plastics_PS_Surface water (micro).csv
│       ├── sinks_EU_Packaging_PS_Surface water (macro).csv
│       └── sinks_EU_Packaging_PS_Surface water (micro).csv
├── README.md
├── cal_T4.py
├── calculation_results.xlsx
├── calculator.py
├── finale_results.xlsx
├── main.py
├── my_microplastic_sim
│   ├── __init__.py
│   ├── config.py
│   ├── exporter.py
│   ├── loader.py
│   └── simulator.py
├── my_water_analysis_sim
│   ├── __init__.py
│   ├── excel_io.py
│   ├── length_calculator.py
│   └── utils.py
└── processing
    ├── em_factor.py
    ├── file_loader.py
    ├── output_formatter.py
    └── type_processor.py
```

---

## Features and Workflow

1. **Excel I/O (`excel_io.py`)**
   - Reads Excel files from the `data/` folder
   - Validates structure and column headers
   - Converts content to pandas DataFrames for processing

2. **Core Calculations (`calculator.py`)**
   - Computes polymer length from physical properties (e.g., density, volume)
   - Performs flow and abrasion analysis based on input parameters

3. **Utilities (`utils.py`)**
   - Provides unit conversions (e.g., mm to µm)
   - Logs important process steps
   - Measures performance execution times

4. **Main Script (`main.py`)**
   - Entry point to the project
   - Reads data → performs calculations → outputs results
   - Easily customizable for further automation or analysis

---

## ⚙️ Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/MahdiAlosh/Microplastic-River-Abrasion.git
cd Microplastic-River-Abrasion
```

> Requires Python 3.10 or higher.

---

## ▶️ How to Use

1. Place your Excel files with experimental data inside the `data/` folder.
2. Make sure they follow the expected format (columns like polymer type, density, abrasion rate, etc.).
3. Run the main script:

```bash
python main.py
```

4. Results will be printed to the console or saved as new Excel/CSV files depending on the configuration.

---

## Example Usage

```python
from src.calculator import calculate_polymer_length

result = calculate_polymer_length(density=0.92, volume=10.5)
print(f"Polymer length: {result:.2f} µm")
```

---
## Requirements

- `pandas`
- `numpy`
- `openpyxl`
- Python built-in libraries (`math`, `time`)
---

## Project Goal

To support scientific research in environmental studies by modeling the formation of microplastics through abrasion mechanisms in river systems using real-world data and computational simulation.
