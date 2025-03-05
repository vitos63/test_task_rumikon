from unittest import TestCase
from simplify_the_expression import simplify_the_expression


class TestAlgebraicCalculator(TestCase):
    def test_1(self):
        expression = "2 * (3 * x + 4 * y) - 7 * y + 9"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "9 + y + 6*x")

    def test_2(self):
        expression = " z + z + 2 + 3 - 2 * z"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "5")

    def test_3(self):
        expression = "3 * (("
        result = simplify_the_expression(expression)
        self.assertEqual(result, "Недопустимое выражение")

    def test_4(self):
        expression = "x * y + 2 * x * y"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "3*x*y")

    def test_5(self):
        expression = "x * 5 - 5 * x"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "0")

    def test_6(self):
        expression = "5 * (x + 1)"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "5 + 5*x")

    def test_7(self):
        expression = "(x + 1) * (x + 1) * (x + 1)"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "1 + 3*x + 3*x*x + x*x*x")

    def test_8(self):
        expression = "(x + (1 + x + x * (x + 1)))"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "3*x + x*x + 1")

    def test_9(self):
        expression = "3 * 5 * 2 * x"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "30*x")

    def test_10(self):
        expression = "3 * y * x - 2 * x * y"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "x*y")

    def test_11(self):
        expression = "(x + 7) * 3"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "21 + 3*x")

    def test_12(self):
        expression = "-5-6-7"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "-18")

    def test_13(self):
        expression = "5-6-7"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "-8")

    def test_14(self):
        expression = "-x-y"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "-y -x")
    

    def test_15(self):
        expression = "-x+y"
        result = simplify_the_expression(expression)
        self.assertEqual(result, "y -x")
