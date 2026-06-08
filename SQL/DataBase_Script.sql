CREATE DATABASE IF NOT EXISTS ecommerce_etl_db;

USE ecommerce_etl_db;

CREATE TABLE IF NOT EXISTS stg_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    brand VARCHAR(100),
    price DECIMAL(10,2),
    discount_percentage DECIMAL(5,2),
    rating DECIMAL(3,2),
    stock INT
);

CREATE TABLE IF NOT EXISTS stg_customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(50),
    age INT,
    gender VARCHAR(50),
    full_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS stg_cart_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT,
    customer_id INT,
    product_id INT,
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10,2),
    total DECIMAL(10,2),
    discount_percentage DECIMAL(5,2),
    discounted_total DECIMAL(10,2),
    cart_total DECIMAL(10,2),
    cart_discounted_total DECIMAL(10,2),
    total_products INT,
    total_quantity INT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
select * from stg_products;