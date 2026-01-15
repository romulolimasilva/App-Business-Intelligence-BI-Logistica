import pandas as pd
import os

# Obtém o diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data", "data_faturmento.xlsx")
file_path = os.path.join(script_dir, "dada", "data_faturmento.xlsx")

df = pd.read_excel(file_path)
print(df.head())