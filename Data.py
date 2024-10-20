import Amazon
import Flipkart
import Fashion
import Groceries
import random


def extract_price(product):
    price_str = product['product_price'][1:].replace(',', '').replace('.','')  # Remove commas and rupee symbol
    return int(price_str)


def get_electronics(user_search,sortBy):
    amazon = Amazon.Amazon(user_search)
    amazon_map = amazon.map_images()
    flipkart = Flipkart.Flipkart(user_search)
    flipkart_map = flipkart.map_images()
    data = flipkart_map + amazon_map
    if sortBy == "1":
        data = sorted(data, key=extract_price)
    else:
        data = sorted(data,key=extract_price,reverse=True)
    return data


def get_fashion(user_search,sortBy):
    amazon = Fashion.Amazon(user_search)
    amazon_map = amazon.map_images()
    flipkart = Fashion.Flipkart(user_search)
    flipkart_map = flipkart.map_images()
    data = flipkart_map + amazon_map
    data = sorted(data, key=extract_price)
    return data


def get_groceries(user_search,sortBy):
    blinkit = Groceries.Blinkit(user_search)
    blinkit_map = blinkit.map_images()
    data = blinkit_map
    data = sorted(data, key=extract_price)
    return data























