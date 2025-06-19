import pandas as pd

# Load Prophet and XGBoost forecast files
prophet_df = pd.read_csv('prophet_all_stores_combined.csv')
xgb_df = pd.read_csv('xgb_all_stores_combined.csv')

# Add a 'model' column to identify the source
prophet_df['model'] = 'Prophet'
xgb_df['model'] = 'XGBoost'

# For consistency, add missing columns to XGBoost that exist in Prophet
xgb_df['lower_ci'] = None
xgb_df['upper_ci'] = None

# Reorder/align columns to match
ordered_columns = ['date', 'store', 'type', 'actual_revenue', 'forecast_revenue', 'lower_ci', 'upper_ci', 'model']
prophet_df = prophet_df[ordered_columns]
xgb_df = xgb_df[ordered_columns]

# Combine both DataFrames
combined_df = pd.concat([prophet_df, xgb_df], ignore_index=True)

# Save to CSV
combined_df.to_csv('forecast_combined_all_models.csv', index=False)

print("Combined file saved as: forecast_combined_all_models.csv")
