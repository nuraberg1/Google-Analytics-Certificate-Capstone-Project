import pandas as pd

# Try opening the CSV file
try:
    df = pd.read_csv("file_name.csv", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("file_name.csv", encoding="ISO-8859-1")
    


# Convert 'Date/Time Column' column to proper datetime format
df['column_name'] = pd.to_datetime(df['column_name'], format='%m/%d/%Y %I:%M:%S %p')

# Ensure BigQuery-compatible timestamp format
df['column_name'] = df['column_name'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Print first few rows
print(df.head())

# Print column names and types
print(df.info()) 
# Save a cleaned version
df.to_csv("clean_file.csv", index=False, encoding="utf-8")

print("✅ Cleaned file saved as 'cleaned_file.csv'")
