
def create_product(name, price):
    return {
        "name": name,
        "price": price, # fixed from name to price value
    }

def print_product(product):
    return f"{product['name']} - ${product['price']}"
    

