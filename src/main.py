import pandas as pd
import numpy as np
import plotly.express as px
import os
from dotenv import load_dotenv
from unidecode import unidecode
import streamlit as st
import sqlite3

load_dotenv()

db_connection = sqlite3.connect(f"{os.environ.get('DB_PATH')}")


def main():
    pass


if __name__ == "__main__":
    main()