import pandas as pd
import numpy as np
import plotly.express as px
import os
import streamlit as st
from dotenv import load_dotenv
from unidecode import unidecode
from extract import extract_data
from transform import transform_data
from load import load_data
from utils import (
    create_dataframe,
    set_columns,
    treat_column_names,
    table_type,
)

load_dotenv()


def main():
    clean_columns = ['dia','grupo_geral','grupo_secundario','exercicio','volume_total_kg']
    df_raw = create_dataframe(extract_data())
    df_raw = set_columns(df_raw)
    df_raw.columns = treat_column_names(df_raw.columns.tolist())
    df_clean = transform_data(df_raw)
    df_clean = df_clean[clean_columns]
    load_data(df=df_raw, table_name=table_type("raw"))
    load_data(df=df_clean, table_name=table_type("clean"))
    df_clean['dia'] = pd.to_datetime(df_clean['dia'], dayfirst=True)


    st.markdown(f"# Acompanhamento academia")
    st.markdown(f"## Exercícios únicos: {df_clean.exercicio.nunique()}")
    top_5_exercices = (df_clean.exercicio.value_counts()[:5]
                    .to_frame()
                    .reset_index()
                    .rename(columns={
                                        'index':'Exercício',
                                        'exercicio':'Total'
                                    }
                            )
                    )
    st.write(
            px.bar(top_5_exercices, 
                    color='Exercício', 
                    text='value', 
                    labels={
                        'value':'Total de execuções', 
                        'index':'Exercício'
                        },
                    title='5 exercícios mais executados'
                    )
        )
    
    total_volume_by_day = df_clean.groupby(['dia','grupo_geral'])['volume_total_kg'].sum().reset_index()
    total_volume_by_day = total_volume_by_day[total_volume_by_day.dia >="2022-12-07"]
    
    st.markdown(f"""### Grupos gerais:""")
    st.markdown("""
                + **A**: Peito e Costas
                + **B**: Pernas
                + **C**: Ombros e braços (biceps, triceps e antebraços)
                """)
    st.write(
        px.bar(total_volume_by_day, 
                x='dia', 
                y='volume_total_kg', 
                color='grupo_geral', 
                text='volume_total_kg', 
                template='plotly_white',
                title='Volume total por grupamento geral',
                labels={
                    "volume_total_kg":"Volume total (kg)",
                    "dia":"Data"
                }
            )
    )


if __name__ == "__main__":
    main()
