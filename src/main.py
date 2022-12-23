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
load_dotenv()


def main():
    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_data(df=df_raw,data_type="raw")
    load_data(df=df_clean,data_type="clean")
    


if __name__ == "__main__":
    main()