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
    retrieve_db_column_names,
    table_type,
)

load_dotenv()


def main():
    df_raw = create_dataframe(extract_data())
    df_raw = set_columns(df_raw)
    df_raw.columns = treat_column_names(df_raw.columns.tolist())
    df_clean = transform_data(df_raw)
    load_data(df=df_raw, table_name=table_type("raw"))
    load_data(df=df_clean, table_name=table_type("clean"))

    x = 4 * 5
    # testando f-strings no streamlit:
    st.markdown(f"# Teste de app: {x}")
    st.write(
        px.line(
            data_frame=df_clean, x="dia", y="volume_total_kg", template="plotly_white"
        )
    )
    st.write(df_clean)
    st.dataframe(df_clean)


if __name__ == "__main__":
    main()
