import csv
import os

def extract_second_last_column(filename):
    """Extracts the second last column from a CSV file without headers."""
    second_last_column = []  # Stores values from the second last column
    
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            if not row:  # Skip empty lines
                continue
            # Get second last element if row has at least 2 columns, else None
            second_last_element = row[-2] if len(row) >= 2 else None
            if second_last_element:
                second_last_column.append(second_last_element)
    return second_last_column

script_dir = os.path.dirname(__file__)
# List of files to process
files = [
    os.path.join(script_dir,'sinks_EU_Clothing (product sector)_PA_Surface water (macro).csv'),
    os.path.join(script_dir,'sinks_EU_Household textiles (product sector)_PA_Surface water (macro).csv'),
    os.path.join(script_dir,'sinks_EU_Technical textiles_PA_Surface water (macro).csv')
]

# Store results for all files
def extract_macro_values():
    """Extracts second last column values from multiple files."""
    results = {}
    print()
    for file in files:
        results[file] = extract_second_last_column(file)
        # print(f"Values for macro:", results[file])
        # print()
    return results

def summarize_macro_results():
    """Calculates and prints the sum of second last column values for each file and overall."""
    results = extract_macro_values()
    sums_per_file = []
    for file, values in results.items():
        values = [float(v) for v in values]
        sum_file = sum(values)
        sums_per_file.append(sum_file)
        print(f"Sum: {sum_file}")
        print()

    sum_all = sum(sums_per_file)
    print(f"Total sum across all files: {sum_all}\n")
    return sum_all

