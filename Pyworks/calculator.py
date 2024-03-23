import math
import sympy as sp

def basic_calculator(expression):
    """
    Perform basic arithmetic calculations on the given expression.

    Args:
        expression (str): The arithmetic expression to evaluate.

    Returns:
        float: The result of the arithmetic calculation.
    """
    try:
        result = eval(expression)
        return result
    except (SyntaxError, NameError, ZeroDivisionError):
        return "Invalid expression"

def sci_cal(expression):
    """
    Perform scientific calculations on the given expression.

    Args:
        expression (str): The scientific expression to evaluate.

    Returns:
        float or str: The result of the scientific calculation, or an error message if the expression is invalid.
    """
    try:
        x = sp.symbols('x')
        result = sp.sympify(expression).evalf()
        return float(result) # Ensure the result is a float
    except (SyntaxError, NameError, ValueError):
        return "Invalid expression"

def solve_equation(equation, variable='x'):
    """
    Solve an algebraic equation for the specified variable.

    Args:
        equation (str): The algebraic equation to solve.
        variable (str, optional): The variable to solve for. Default is 'x'.

    Returns:
        str: The solution to the equation, or an error message if the equation is invalid.
    """
    try:
        x = sp.symbols(variable)
        expr = sp.sympify(equation)
        solution = sp.solveset(expr, x)
        return str(solution)
    except (SyntaxError, NameError, ValueError):
        return "Invalid equation"

def plot_function(function, variable='x', start=-10, end=10):
    """
    Plot a mathematical function over a specified range.

    Args:
        function (str): The mathematical function to plot.
        variable (str, optional): The variable used in the function. Default is 'x'.
        start (float, optional): The starting value of the range. Default is -10.
        end (float, optional): The ending value of the range. Default is 10.

    Returns:
        None: This function displays the plot using matplotlib.
    """
    try:
        import matplotlib.pyplot as plt
        x = sp.symbols(variable)
        expr = sp.sympify(function)
        x_vals = sp.linspace(start, end, 100)
        y_vals = [expr.subs(x, val) for val in x_vals]
        plt.plot(x_vals, y_vals)
        plt.xlabel(variable)
        plt.ylabel('f(' + variable + ')')
        plt.title(function)
        plt.grid(True)
        plt.show()
    except (SyntaxError, NameError, ValueError, ImportError):
        print("Error: Unable to plot the function")

def matrix_operations(operation, matrix1, matrix2=None):
    """
    Perform matrix operations such as addition, subtraction, multiplication, transpose, and inverse.

    Args:
        operation (str): The matrix operation to perform ('add', 'subtract', 'multiply', 'transpose', 'inverse').
        matrix1 (list): The first matrix represented as a list of lists.
        matrix2 (list, optional): The second matrix represented as a list of lists. Required for addition, subtraction, and multiplication.

    Returns:
        list or str: The result of the matrix operation as a list of lists, or an error message if the operation is invalid or the matrices are incompatible.
    """
    try:
        matrix1 = sp.Matrix(matrix1)
        if operation in ['add', 'subtract', 'multiply']:
            matrix2 = sp.Matrix(matrix2)
            if operation == 'add':
                result = matrix1 + matrix2
            elif operation == 'subtract':
                result = matrix1 - matrix2
            else:
                result = matrix1 * matrix2
        elif operation == 'transpose':
            result = matrix1.T
        elif operation == 'inverse':
            result = matrix1.inv() # Corrected to use inv()
        else:
            return "Invalid operation"
        return result.tolist()
    except (ValueError, TypeError, Exception): # Corrected to catch a more general exception
        return "Invalid matrices"