import unittest

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:

    def __init__(self, *args):
        self.arg = args

    def get_total_price(self):

        out_price = 0
        my_tuple = self.arg[0]
        for i in range(len(my_tuple)):
            current_count, current_price = my_tuple[i].count, my_tuple[i].price
            # print(self.arg[0][i].price, self.arg[0][i].count)

            if current_count > 20:  # more than 20	50%
                out_price += (current_price * current_count) * 0.5

            elif current_count == 20:  # at least 20	30%
                out_price += (current_price * current_count) * 0.7

            elif current_count >= 10:  # at least 10	20%
                out_price += (current_price * current_count) * 0.8

            elif current_count >= 7:  # at least 7	10%
                out_price += (current_price * current_count) * 0.9

            elif current_count >= 5:  # at least 5	5%
                out_price += (current_price * current_count) * 0.95

            else:
                out_price += current_price * current_count

        return out_price
class CartTest(unittest.TestCase):
    test_prod = (Product('p1', 10, 4),
                 Product('p2', 100, 5),
                 Product('p3', 200, 6),
                 Product('p4', 300, 7),
                 Product('p5', 400, 9),
                 Product('p6', 500, 10),
                 Product('p7', 1000, 20))
    # cart = Cart(products)

    def test_plus(self, test_prod1=test_prod):
        self.assertEqual(Cart(test_prod1).get_total_price(), 24785.0)
