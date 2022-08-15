def shopping_cart(*args):
    result = ""
    products = {"Pizza": [], "Soup": [], "Dessert": []}
    for element in args:
        if element == "Stop":
            break
        meal, product = element[0:]
        if meal == "Pizza" and len(products["Pizza"]) < 4 and product not in products["Pizza"]:
            products["Pizza"].append(product)
        elif meal == "Soup" and len(products["Soup"]) < 3 and product not in products["Soup"]:
            products["Soup"].append(product)
        elif meal == "Dessert" and len(products["Dessert"]) < 2 and product not in products["Dessert"]:
            products["Dessert"].append(product)
    if len(products["Pizza"]) or len(products["Soup"]) or len(products["Dessert"]):
        sorted_products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))
        for key, value in sorted_products:
            result += f"{key}:\n"
            for v in sorted(value):
                result += f" - {v}\n"
    else:
        result = "No products in the cart!"
    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
