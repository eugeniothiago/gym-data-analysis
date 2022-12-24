import pandas as pd
from unidecode import unidecode
import sqlite3


def create_dataframe(data: list) -> pd.DataFrame:
    """Create a Pandas Dataframe from an list of lists

    Args:
        data (list): List of data

    Returns:
        pd.DataFrame: A pandas dataframe
    """
    df = pd.DataFrame(data)
    return df


def set_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Sets the first line of the dataset as the columns names

    Args:
        df (pd.DataFrame): pandas dataframe

    Returns:
        pd.DataFrame: pandas dataframe
    """
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def treat_column_names(cols: list) -> list:
    return [unidecode(col.lower().replace(" ", "_").replace("\n", "")) for col in cols]


def retrieve_db_table_column_names(
    db_connection: sqlite3.Connection, table_name: str
) -> list:
    """retrieve local database columns names in a list"""
    table = table_name
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"PRAGMA table_info({table})")
    db_connection.commit()
    column_list = db_cursor.fetchall()
    return [col[1] for col in column_list]


def table_type(type: str) -> object:
    if type == "clean":
        return "gym_data_clean"
    elif type == "raw":
        return "gym_data_raw"


if __name__ == "__name__":
    create_dataframe(),
    set_columns(),
    treat_column_names(),
    retrieve_db_table_column_names(),
    table_type()
