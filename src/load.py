import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.environ.get("DB_PATH")
db_connection = sqlite3.connect(db_path)
db_cursor = db_connection.cursor()


def drop_db_tables(
    db_connection: sqlite3.Connection, db_cursor: sqlite3.Cursor
) -> None:
    db_cursor.executescript(
        f"""
                            DROP TABLE IF EXISTS gym_data;
                            DROP TABLE IF EXISTS gym_data_clean;
                            DROP TABLE IF EXISTS gym_data_raw;
                            """
    )
    db_connection.commit()
    return None


def load_data(df: pd.DataFrame, table_name: str) -> None:
    df.to_sql(table_name, db_connection, if_exists="replace", index=False)
    return None


if __name__ == "__main__":
    load_data(),
    drop_db_tables()
