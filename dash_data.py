import streamlit as st
import pandas as pd
import os

# Configuração da página para modo amplo (wide)
st.set_page_config(page_title="Dashboard Logística", layout="wide")

# Criar o painel de apresentação
st.title("Painel de apresentação")

# Carregar os dados 
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dada", "data_faturmento.xlsx")
df = pd.read_excel(file_path)

# Exibir os dados
st.write(df)
