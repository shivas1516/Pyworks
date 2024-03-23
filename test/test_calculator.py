import unittest
import sympy as sp
from Pyworks.calculator import *

class TestCalculatorFunctions(unittest.TestCase):
    def test_basic_calculator(self):
        # Test valid expressions
        self.assertEqual(basic_calculator("2 + 3"), 5)
        self.assertEqual(basic_calculator("10 - 4"), 6)
        self.assertEqual(basic_calculator("5 * 6"), 30)
        self.assertEqual(basic_calculator("10 / 2"), 5)

        # Test invalid expressions
        self.assertEqual(basic_calculator("10 / 0"), "Invalid expression")
        self.assertEqual(basic_calculator("abc + 5"), "Invalid expression")

    def test_sci_cal(self):
        # Test valid expressions
        self.assertEqual(sci_cal("sqrt(25)"), 5)
        self.assertEqual(sci_cal("sin(pi/2)"), 1)
        self.assertEqual(sci_cal("log(10)"), sp.log(10))

        # Test invalid expressions
        self.assertEqual(sci_cal("sin(abc)"), "Invalid expression")
        self.assertEqual(sci_cal("log(-1)"), "Invalid expression")

    def test_solve_equation(self):
        # Test valid equations
        self.assertEqual(solve_equation("x**2 - 4", "x"), "{-2, 2}")
        self.assertEqual(solve_equation("2*x - 8", "x"), "{4}")
        self.assertEqual(solve_equation("x**2 + 6*x + 9", "x"), "{-3}")

        # Test invalid equations
        self.assertEqual(solve_equation("sqrt(x) + 3", "x"), "Invalid equation")
        self.assertEqual(solve_equation("log(x) - 2", "x"), "Invalid equation")

    def test_matrix_operations(self):
        # Test matrix addition
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        self.assertEqual(matrix_operations("add", matrix1, matrix2), [[6, 8], [10, 12]])

        # Test matrix subtraction
        self.assertEqual(matrix_operations("subtract", matrix1, matrix2), [[-4, -4], [-4, -4]])

        # Test matrix multiplication
        self.assertEqual(matrix_operations("multiply", matrix1, matrix2), [[19, 22], [43, 50]])

        # Test matrix transpose
        self.assertEqual(matrix_operations("transpose", matrix1), [[1, 3], [2, 4]])

        # Test matrix inverse
        matrix3 = [[1, 2], [3, 4]]
        self.assertEqual(matrix_operations("inverse", matrix3), [[-2.0, 1.0], [1.5, -0.5]])

if __name__ == '__main__':
    unittest.main()
