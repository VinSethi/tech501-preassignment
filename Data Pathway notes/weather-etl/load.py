import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    return create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}")

def load_data(df, table_name="weather"):
    engine = get_engine()
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
