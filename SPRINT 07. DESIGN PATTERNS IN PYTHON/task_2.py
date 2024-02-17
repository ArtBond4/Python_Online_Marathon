class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy(price) if discount_strategy else price

    def __str__(self):
        return self.price_after_discount()

    def price_after_discount(self):
        return f'Price: {self.price}, price after discount: {self.discount_strategy}'


def on_sale_discount(order):
    return order * 0.5
def twenty_percent_discount(order):
    return order * 0.8
