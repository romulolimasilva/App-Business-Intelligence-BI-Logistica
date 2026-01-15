import pandas as pd
import streamlit as st
import os

# Configuração da página
st.set_page_config(layout="wide", page_title="Dashboard Logística")

# Carregar os dados
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dada", "data_faturmento.xlsx")

if os.path.exists(file_path):
    df = pd.read_excel(file_path)

    # --- STORYTELLING: Título e Contexto ---
    st.title("📊 Dashboard de Faturamento e Logística")
    st.markdown("Este painel apresenta os indicadores chave de desempenho para apoio à tomada de decisão.")
    st.markdown("---")

    # --- FILTROS: Barra Lateral ---
    st.sidebar.header("Filtros de Análise")

    # Filtro de Ano
    if "ANO" in df.columns:
        anos = sorted(df["ANO"].unique())
        selected_year = st.sidebar.selectbox("Selecione o Ano:", ["Todos"] + list(anos))

        if selected_year != "Todos":
            df = df[df["ANO"] == selected_year]
            st.info(f"📌 Dados filtrados para o ano **{selected_year}**")

    # Filtro de texto (MÊS ou outros campos categóricos)
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if not cat_cols.empty:
        col_filtro = st.sidebar.selectbox("Filtrar por campo categórico:", ["Nenhum"] + list(cat_cols))
        if col_filtro != "Nenhum":
            val_filtro = st.sidebar.selectbox(f"Selecione {col_filtro}:", ["Todos"] + list(df[col_filtro].unique()))
            if val_filtro != "Todos":
                df = df[df[col_filtro] == val_filtro]
                st.info(f"📌 Visualizando dados filtrados por **{col_filtro}: {val_filtro}**")

    # --- KPIs: Os Grandes Números Primeiro ---
    st.subheader("📈 Indicadores Gerais")
    num_cols = df.select_dtypes(include=['number']).columns
    
    kpi_cols = st.columns(min(len(num_cols) + 1, 5))
    kpi_cols[0].metric("Total de Registros", len(df))
    
    for i, col in enumerate(num_cols[:4]):
        total = df[col].sum()
        kpi_cols[i + 1].metric(f"Total {col}", f"{total:,.2f}")

    st.markdown("---")

    # --- DETALHES: Gráficos em Grid ---
    st.subheader("🔍 Análise Detalhada por Variável")

    cols = st.columns(4)

    for i, col in enumerate(df.columns):
        with cols[i % 4]:
            st.markdown(f"**{col}**")
            
            if pd.api.types.is_numeric_dtype(df[col]):
                st.line_chart(df[col])
                st.caption(f"Média: {df[col].mean():.2f}")
            else:
                counts = df[col].value_counts()
                st.bar_chart(counts)
                if not counts.empty:
                    st.caption(f"Maior ocorrência: {counts.index[0]}")
else:
    st.error(f"Arquivo não encontrado: {file_path}")
