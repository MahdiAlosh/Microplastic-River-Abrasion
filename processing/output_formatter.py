import pandas as pd

# def print_total_lengths(result_df):
    
#     print("\nTotal Length by Water Body Type:\n" + "="*32)
#     for _, row in result_df.iterrows():
#         print(f"{row['Gewässertyp']}: {row['Länge']} km")
    
#     print(f"\nTotal Length of All Water Bodies: {result_df['Länge'].sum():.2f} km")

def export_results(all_results, result_df):
    df = pd.DataFrame(all_results)
    numeric_cols = df.columns.drop("Type")

    for col in numeric_cols:
        if col == "Length (km)":
            df[col] = df[col].map("{:.2f}".format)
        else:
            df[col] = df[col].map("{:.6f}".format)

    new_row = {"Type": "Total length of all rivers", "Length (km)": result_df["Länge"].sum()}
    for col in numeric_cols:
        if col != "Length (km)":
            new_row[col] = " "

    all_results.append(new_row)
    df = pd.DataFrame(all_results)
    # new_df = pd.DataFrame([new_row])
    # df = pd.concat([df, new_df], ignore_index=True)

    output_file = "calculation_results.xlsx"
    df.to_excel(output_file, index=False)
    print(f"\nResults exported to {output_file}\n")
