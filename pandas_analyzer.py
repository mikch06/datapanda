import pandas as pd
import os

# Overall output
output_file = "output.csv"

# Delete output file at startup
if os.path.exists(output_file):
    os.remove(output_file)

print("Start data analyzer")

# Pandas display properties -> output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)
pd.set_option('display.max_colwidth', None)

# TODO: add xml parsing!

# Read input file types
def read_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()  # Filesuffix find
    
    if ext in ['.csv', '.txt']:  # CSV or TXT
        return pd.read_csv(filepath, sep=None, engine='python')  # Separation
    elif ext in ['.xls', '.xlsx']:  # Excel
        return pd.read_excel(filepath)
    elif ext == '.json':  # JSON
        return pd.read_json(filepath)
    #elif ext == '.parquet':  # Parquet
     #   return pd.read_parquet(filepath)
    else:
        raise ValueError(f"Format {ext} not supported.")



# Recursive directory search
def load_files_recursive(folder_path):
    dataframes = {}
    
    for root, _, files in os.walk(folder_path):  # recursive search
        for file in files:
            filepath = os.path.join(root, file)
            try:
                dataframes[filepath] = read_file(filepath)
                print(f"✅ {filepath} loaded successfully.")
            except Exception as e:
                print(f"❌ Load of {filepath} failed: {e}")

    return dataframes

# Example data call
folder_path = "data"
dataframes = load_files_recursive(folder_path)

# Loop to print output on std. shell
for path, df in dataframes.items():

    with open(output_file, mode="a", encoding="utf-8") as f:
        f.write(f"# File: {path}\n")

    # Print all output to output.csv file
    df.to_csv(output_file, mode='a')
print("\nRun has finished.")
