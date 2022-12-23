import pandas as pd
from unidecode import unidecode


def create_dataframe(data:list) -> pd.DataFrame:
    df = pd.DataFrame(data)
    return df

def set_columns(df:pd.DataFrame)-> pd.DataFrame:
    # transform the list of values into a dataframe
    # and define the first row as the colums names
    df.columns = df.iloc[0]
    df = df[1:]
    return df

def treat_column_names(df:pd.DataFrame)->pd.DataFrame:
    df.columns = [
    unidecode(col.lower().replace(" ", "_").replace("\n", ""))
    for col in df.columns.tolist()
    ]
    return df

if __name__=="__name__":
    create_dataframe(),
    set_columns(),
    treat_column_names()