import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()


def load_data(df: pd.DataFrame, data_type: str) -> None:
    db_path = os.environ.get("DB_PATH")
    db_connection = sqlite3.connect(db_path)
    db_cursor = db_connection.cursor()
    table_name = "gym_data"
    if data_type == "raw":
        table_name = "gym_data_raw"
    elif data_type == "clean":
        table_name = "gym_data_clean"
    df.to_sql(table_name, db_connection, if_exists="replace", index_label="entry_id")


if __name__ == "__main__":
    load_data()
