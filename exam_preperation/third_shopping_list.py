def shopping_list(budget, **kwargs):
    shop_list = []
    if budget < 100:
        return "You do not have enough budget."
    for product_name, product_price in kwargs.items():
        total_price = product_price[0] * product_price[1]
        if len(shop_list) == 5:
            break
        if budget >= total_price:
            shop_list.append(f"You bought {product_name} for {total_price:.2f} leva.")
            budget -= total_price
    return '\n'.join(shop_list)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
