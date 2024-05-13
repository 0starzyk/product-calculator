import numpy as np
from src.config import Config


def is_valid_product_data(product: dict):
    if len(product) != Config.NUMBER_OF_PRODUCT_PROPERTIES.value:
        return False
    if not product["name"].isalpha():
        return False
    if product["price"] <= 0.0:
        return False
    return True


def autopct_format(values: list) -> callable:
    def my_format(pct):
        total = sum(values)
        percent = round(pct)
        value = round(pct * total / 100.0, 2)
        return f"{value} PLN\n({percent}%)"
    return my_format


def get_values_and_labels_from_products(products: list) -> tuple:
    available_categories = np.unique([product["category"] for product in products])
    accumulated_prices = {category: 0.0 for category in available_categories}
    for product in products:
        accumulated_prices[product["category"]] += product["price"]
    values = list(accumulated_prices.values())
    labels = list(accumulated_prices.keys())
    return values, labels
