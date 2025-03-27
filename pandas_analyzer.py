import pandas as pd
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)
pd.set_option('display.max_colwidth', None)



def read_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()  # Dateiendung ermitteln
    
    if ext in ['.csv', '.txt']:  # CSV oder Textdatei
        return pd.read_csv(filepath, sep=None, engine='python')  # Automatische Trennung
    elif ext in ['.xls', '.xlsx']:  # Excel
        return pd.read_excel(filepath)
    elif ext == '.json':  # JSON
        return pd.read_json(filepath)
    elif ext == '.parquet':  # Parquet
        return pd.read_parquet(filepath)
    else:
        raise ValueError(f"Dateiformat {ext} wird nicht unterstützt.")



# Verzeichnis rekursiv durchsuchen
def load_files_recursive(folder_path):
    dataframes = {}
    
    for root, _, files in os.walk(folder_path):  # Rekursive Suche
        for file in files:
            filepath = os.path.join(root, file)
            try:
                dataframes[filepath] = read_file(filepath)
                print(f"✅ {filepath} erfolgreich geladen.")
            except Exception as e:
                print(f"❌ Fehler beim Laden von {filepath}: {e}")

    return dataframes

# Example data call
folder_path = "data"
dataframes = load_files_recursive(folder_path)


# Loop to print output on std. shell
for path, df in dataframes.items():
    print(f"--- File: {path} ---")
    print(df)
    print("\n")  # Leerzeile zur Trennung

    # Print all output to output.csv file
    df.to_csv("output.csv", mode='a')

#print(df.to_string())    