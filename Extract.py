import requests
import pandas as pd


def fetch_api_data(url, key, limit=100):
    params = {"limit": limit}

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    return pd.DataFrame(data[key])


def extract_products(limit=100):
    url = "https://dummyjson.com/products"
    return fetch_api_data(url, "products", limit)


def extract_carts(limit=50):
    url = "https://dummyjson.com/carts"
    return fetch_api_data(url, "carts", limit)


def extract_users(limit=100):
    url = "https://dummyjson.com/users"
    return fetch_api_data(url, "users", limit)