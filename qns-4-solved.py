import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df_row_merged = pd.concat([df1, df2], ignore_index=True)
    return df_row_merged
    
