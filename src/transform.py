import pandas as pd
import numpy as np
import os
from unidecode import unidecode
from dotenv import load_dotenv
from utils import treat_column_names, set_columns
load_dotenv()

clean_columns = ['dia',]
def treat_custom_values(x):
    x = eval(x)
    if type(x)==int:
        return x
    elif type(x) == tuple and type(x[0])==tuple:
        x = list(x)
        return sum(map(sum,x))
    else:
        return sum(x)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    #treating numeric columns
    df[['series','repeticoes','peso']] = (df[['series','repeticoes','peso']]
                                        .replace(" ",0)
                                        .replace("",0)
                                        .fillna(0)
                                        .astype('float'))
    df = df.drop("volume_total", axis=1)
    df["series_personalizadas_calculadas"] = (
    df["series_personalizadas"]
    .fillna("0")
    .map(treat_custom_values))
    df["volume_total_kg"] = (df["series"] * df["repeticoes"] * df["peso"]) + df[
        "series_personalizadas_calculadas"
    ]
    df["dia"] = df["dia"].fillna(method="ffill")
    return df

if __name__=="__main__":
    transform_data()