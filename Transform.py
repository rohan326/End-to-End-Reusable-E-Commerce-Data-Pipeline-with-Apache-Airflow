import pandas as pd


def clean_products(df):
    df = df.copy()

    df = df[[
        "id", "title", "category", "brand", "price",
        "discountPercentage", "rating", "stock"
    ]]

    df.rename(columns={
        "id": "product_id",
        "title": "product_name",
        "discountPercentage": "discount_percentage"
    }, inplace=True)

    df["product_name"] = df["product_name"].str.strip()
    df["category"] = df["category"].str.lower().str.strip()
    df["brand"] = df["brand"].fillna("Unknown")

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["discount_percentage"] = pd.to_numeric(df["discount_percentage"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")

    df = df.drop_duplicates(subset=["product_id"])
    df = df.dropna(subset=["product_id", "product_name", "price"])

    return df


def clean_users(df):
    df = df.copy()

    df = df[["id", "firstName", "lastName", "email", "phone", "age", "gender"]]

    df.rename(columns={
        "id": "customer_id",
        "firstName": "first_name",
        "lastName": "last_name"
    }, inplace=True)

    df["full_name"] = df["first_name"] + " " + df["last_name"]
    df["email"] = df["email"].str.lower().str.strip()
    df["gender"] = df["gender"].str.lower().str.strip()

    df = df.drop_duplicates(subset=["customer_id"])
    df = df.dropna(subset=["customer_id", "email"])

    return df


def clean_carts(df):
    rows = []

    for _, cart in df.iterrows():
        cart_id = cart["id"]
        customer_id = cart["userId"]
        total = cart["total"]
        discounted_total = cart["discountedTotal"]
        total_products = cart["totalProducts"]
        total_quantity = cart["totalQuantity"]

        for product in cart["products"]:
            rows.append({
                "cart_id": cart_id,
                "customer_id": customer_id,
                "product_id": product["id"],
                "product_name": product["title"],
                "quantity": product["quantity"],
                "price": product["price"],
                "total": product["total"],
                "discount_percentage": product["discountPercentage"],
                "discounted_total": product["discountedTotal"],
                "cart_total": total,
                "cart_discounted_total": discounted_total,
                "total_products": total_products,
                "total_quantity": total_quantity
            })

    clean_df = pd.DataFrame(rows)

    clean_df = clean_df.drop_duplicates()
    clean_df = clean_df.dropna(subset=["cart_id", "customer_id", "product_id"])

    return clean_df