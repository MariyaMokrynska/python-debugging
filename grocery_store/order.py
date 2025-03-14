


def create_order(products, customer_name):
    return {
        "customer_name": customer_name,
        "products": products,
    }

def add_product(order, product):
    order["products"].append(product)

def calculate_total(order):
    total = 0
    for i in range(0, len(order["products"])): # fixed range starting from 0
        total += order["products"][i]["price"]

    return total
