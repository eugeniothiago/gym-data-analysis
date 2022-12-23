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
from utils import set_columns, treat_column_names, create_dataframe

load_dotenv()


def main():
    df_raw = create_dataframe(extract_data())
    df_raw = set_columns(df_raw)
    df_raw = treat_column_names(df_raw)
    df_clean = transform_data(df_raw)
    load_data(df=df_raw, data_type="raw")
    load_data(df=df_clean, data_type="clean")


if __name__ == "__main__":
    main()
