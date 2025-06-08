# 🌊 Microplastic River Abrasion

This project analyzes microplastic abrasion in river environments using experimental Excel data. It is intended to simulate and evaluate how microplastics may form and disperse based on physical and chemical properties of polymers, abrasion parameters, and river characteristics.

---

## 🧩 Project Structure

```
Microplastic-River-Abrasion/
│
├── data/                   # Input Excel files with polymer and river data
├── src/
│   ├── excel_io.py         # Handles reading and writing Excel files using pandas
│   ├── calculator.py       # Contains all scientific calculations related to abrasion and polymer analysis
│   └── utils.py            # Helper functions (e.g., unit conversions, performance timing)
│
├── main.py                 # Main script that connects all modules and runs the analysis
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation (this file)
```

---

## 🚀 Features and Workflow

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
pip install -r requirements.txt
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

## 🧪 Example Usage

```python
from src.calculator import calculate_polymer_length

result = calculate_polymer_length(density=0.92, volume=10.5)
print(f"Polymer length: {result:.2f} µm")
```

---

## 📦 Requirements

- `pandas`
- `numpy`
- `openpyxl`
- Python built-in libraries (`math`, `time`)

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🎯 Project Goal

To support scientific research in environmental studies by modeling the formation of microplastics through abrasion mechanisms in river systems using real-world data and computational simulation.
