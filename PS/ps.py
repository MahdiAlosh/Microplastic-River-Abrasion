from PS.scr.macro import summarize_macro_results
from PS.scr.micro import summarize_micro_results
from PS.scr.ps_summary_df import create_summary_dataframe

def ps():
    # Assuming macro and micro results are already calculated
    macro_sum = summarize_macro_results()
    micro_sum = summarize_micro_results()

    # Create summary DataFrame
    ps_summary_df = create_summary_dataframe(macro_sum, micro_sum)

    return ps_summary_df
    # Save to Excel
    # try:
    #     summary_df.to_excel('summary_results.xlsx', index=False, sheet_name='PS')
    #     print("Summary results saved to 'summary_results.xlsx'.\n")
    # except Exception as e:
    #     print(f"Error saving Excel file: {e}")

# if __name__ == "__main__":
#     main()