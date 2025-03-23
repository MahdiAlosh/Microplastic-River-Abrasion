import pandas as pd

def calculate_total_length_by_type(excel_file_path, length_column="Länge", type_column="Gewässertyp"):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_path)
        
        df = df.iloc[:-2]

        # Ensure the required columns exist
        if length_column not in df.columns or type_column not in df.columns:
            raise ValueError(f"Required columns '{length_column}' or '{type_column}' not found in the Excel file.")
        
        # Convert length values to numeric, handling potential formatting issues
        df[length_column] = pd.to_numeric(df[length_column], errors='coerce')
        
        # Group by water body type and sum the lengths
        result = df.groupby(type_column)[length_column].sum().reset_index()
        
        # Sort by total length in descending order
        result = result.sort_values(by=length_column, ascending=False)
        
        # Format the results with two decimal places
        result[length_column] = result[length_column].round(2)
        
        return result
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    # Specify the path to your Excel file
    excel_file_length = "C:\\Users\\Ali Al Mahdi\\Desktop\\HTWD\\5 Semester\\Arbeit\\2025-02-28 Wasserkoerper Navigator 2022-2027 - Flüsse.xlsx"
    
    # Calculate total lengths by water body type
    result_df = calculate_total_length_by_type(excel_file_length)
    
    if result_df is not None:
        print("\nTotal Length by Water Body Type:")
        print("================================")
        
        for index, row in result_df.iterrows():
            water_type = row["Gewässertyp"]
            total_length = row["Länge"]
            print(f"{water_type}: {total_length} km")
        
        print(f"\nTotal Length of All Water Bodies: {result_df['Länge'].sum():.2f} km")

    # print(f"{type(result_df)} \n {result_df}")

if __name__ == "__main__":
    main()