from Extract import extract_products, extract_carts, extract_users
from Transform import clean_products, clean_carts, clean_users
from Load import load_to_staging


def run_etl_pipeline():
    raw_products = extract_products(limit=100)
    raw_carts = extract_carts(limit=50)
    raw_users = extract_users(limit=100)

    clean_product_df = clean_products(raw_products)
    clean_cart_df = clean_carts(raw_carts)
    clean_user_df = clean_users(raw_users)

    print(f"Products processed: {len(clean_product_df)}")
    print(f"Cart items processed: {len(clean_cart_df)}")
    print(f"Users processed: {len(clean_user_df)}")

    load_to_staging(clean_product_df, clean_user_df, clean_cart_df)


if __name__ == "__main__":
    run_etl_pipeline()