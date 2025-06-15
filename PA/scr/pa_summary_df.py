import pandas as pd

def create_summary_dataframe(macro_sum, micro_sum):
    """Creates a DataFrame summarizing macro and micro results."""
    data = {
        ' ': ['Macro', 'Micro'],
        'Total Sum in kg': [macro_sum, micro_sum]
    }
    df = pd.DataFrame(data)
    return df