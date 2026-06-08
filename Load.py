from sqlalchemy import create_engine
from urllib.parse import quote_plus


def get_mysql_engine():
    username = "root"
    password = quote_plus("sai@#1609R")
    host = "localhost"
    port = "3306"
    database = "ecommerce_etl_db"

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    )

    return engine


def load_to_staging(products_df, users_df, carts_df):
    engine = get_mysql_engine()

    products_df.to_sql(
        name="stg_products",
        con=engine,
        if_exists="replace",
        index=False
    )

    users_df.to_sql(
        name="stg_customers",
        con=engine,
        if_exists="replace",
        index=False
    )

    carts_df.to_sql(
        name="stg_cart_items",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into MySQL staging tables successfully.")