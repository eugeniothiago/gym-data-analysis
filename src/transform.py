import pandas as pd
import numpy as np
import os
from unidecode import unidecode
from dotenv import load_dotenv
load_dotenv()

def transform_data(df:pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(df)
    df.columns = df.iloc[0]
    df = df[1:]
    
    #renaming columns
    df.columns = [
    unidecode(col.lower().replace(" ", "_").replace("\n", ""))
    for col in df.columns.tolist()
    ]
    #treating numeric columns
    df[['series','repeticoes','peso']] = df[['series','repeticoes','peso']].fillna(0).astype('float', errors='ignore')
    df = df.drop("volume_total", axis=1)
    df["series_personalizadas"] = df["series_personalizadas"].fillna("0")
    df["series_personalizadas_calculadas"] = (
        df["series_personalizadas"]
        .apply(lambda x: eval(str(x).replace("x", "*")))
        .apply(lambda x: sum(x) if type(x) != int else x)
    )
    df["volume_total_kg"] = (df["series"] * df["repeticoes"] * df["peso"]) + df[
        "series_personalizadas_calculadas"
    ]
    df["dia"] = df["dia"].fillna(method="ffill")
    return df

if __name__=="__main__":
    transform_data()