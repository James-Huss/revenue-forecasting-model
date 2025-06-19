import os
import pandas as pd

# Define the folder containing individual store CSVs
folder_path = 'xgb_store_forecasts'

# List of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Load and combine all CSVs
df_list = []
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    df_list.append(df)

# Concatenate all into one DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Save to a single CSV
output_filename = 'xgb_all_stores_combined.csv'
combined_df.to_csv(output_filename, index=False)

print(f"Combined CSV saved as '{output_filename}' with {combined_df.shape[0]} rows.")
