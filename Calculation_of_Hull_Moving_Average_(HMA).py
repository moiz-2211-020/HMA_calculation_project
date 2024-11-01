import pandas as pd
import numpy as np


def calculate_HM(file_path, output_csv_path):
    # Read the Excel file into a DataFrame
    excel_file = pd.read_excel(file_path)
    df = pd.DataFrame(excel_file)

    # Trim whitespace from column names
    df.columns = df.columns.str.strip()

    # Remove duplicated columns if any
    df = df.loc[:, ~df.columns.duplicated()]

    # Calculate Change, Gain, and Loss
    df["Change"] = np.round(df["Input"].diff(), 2)
    df["Gain"] = np.round(np.where(df["Change"] > 0, df["Change"], 0), 2)
    df["Loss"] = np.round(np.where(df["Change"] < 0, df["Change"].abs(), 0), 2)

    # Initialize Avg Gain and Avg Loss with NaN
    df["Avg Gain"] = np.nan
    df["Avg Loss"] = np.nan

    # Calculate Avg Gain and Avg Loss for the first 14 days
    if len(df) > 14:  # Check if there are at least 14 rows
        # Calculate the first Avg Gain and Avg Loss values for the first 14 entries
        df.loc[14, "Avg Gain"] = round((df["Gain"].iloc[:14].mean()),2) # Average of first 14 Gain values
        df.loc[14, "Avg Loss"] = round((df["Loss"].iloc[:14].mean()),2)  # Average of first 14 Loss values

        # Calculate Avg Gain and Avg Loss for the rest of the entries
        for i in range(15, len(df)):
            df.loc[i, "Avg Gain"] = ((df.loc[i - 1, "Avg Gain"] * 13 + df.loc[i, "Gain"]) / 14)
            df.loc[i, "Avg Loss"] = ((df.loc[i - 1, "Avg Loss"] * 13 + df.loc[i, "Loss"]) / 14)

    df["HM"] = np.where(df["Avg Loss"] == 0, np.nan, (df["Avg Gain"] / df["Avg Loss"]))
    df["HM"] = df["HM"].round(2)
    # Calculate 14-day HMA
    df['14-day HMA'] = np.where(df['Avg Loss'] == 0, 100,(100 - (100 / (1 + df['HM']))))
    df['14-day HMA'] = df['14-day HMA'].round(2)

    df["Avg Gain"] = df["Avg Gain"].round(2)
    df["Avg Loss"] = df["Avg Loss"].round(2)
    # Save the resulting DataFrame to a CSV file
    df.to_csv(output_csv_path, index=False)
    return df
csv_file = "/Users/moiz/Documents/espark_consultant_group/uploads/hma_output.csv"
excel_file = "/Users/moiz/Documents/espark_consultant_group/uploads/hma.xlsx"
print(calculate_HM(excel_file,csv_file))
