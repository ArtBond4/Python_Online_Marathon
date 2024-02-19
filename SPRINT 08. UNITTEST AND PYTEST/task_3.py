def quadratic_equation(a, b, c):
    try:
        discriminant = b ** 2 - 4 * a * c
    except TypeError:
        raise TypeError("Errorrrrrrrrrrrrrrrrr!!!!!!!")
    if discriminant < 0:
        return None
    elif discriminant == 0:
        try:
            return -b / (2 * a)
        except ZeroDivisionError:
            raise ValueError

    x1 = float((-b + discriminant ** 0.5) / (2 * a))
    x2 = float((-b - discriminant ** 0.5) / (2 * a))

    return x1, x2


#
# print(quadratic_equation(2, 1, -1) == (0.5, -1.0))
# print(quadratic_equation(1, -4, 4) == 2.0)

class QuadraticEquationTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(quadratic_equation(1, 3, -4), (1.0, -4.0))

    def test_2(self):
        with self.assertRaises(TypeError) as e:
            quadratic_equation("1", -21, 66)
        self.assertEqual("Errorrrrrrrrrrrrrrrrr!!!!!!!", e.exception.args[0])



    def test_3(self):
        self.assertEqual(quadratic_equation(32, 28, -11), (0.2940437444199766, -1.1690437444199766))

    def test_4(self):
        self.assertEqual(quadratic_equation(-96, 61, -4), (0.07425008557249495, 0.5611665810941717))

    def test_5(self):
        self.assertEqual(quadratic_equation(55, 11, 82), None)

    def test_6(self):
        self.assertEqual(quadratic_equation(92, -84, -73), (1.4574664724540292, -0.5444229941931598))

    def test_7(self):
        self.assertEqual(quadratic_equation(12, -20, 9), None)

    def test_8(self):
        self.assertEqual(quadratic_equation(18, 40, 78), None)

    def test_9(self):
        self.assertEqual(quadratic_equation(-39, -7, 88), (-1.5945572553880516, 1.415070075900872))
