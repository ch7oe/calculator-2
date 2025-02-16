"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 + num2."""

    return num1 + num2


def subtract(num1, num2):
    """Return the value of num1 minus num2."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""

    return num1 * num2


def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of num1."""

    return num1 * num1


def cube(num1):
    """Return the cube of num1."""

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2


def add_multi(num1, num2, num3):
    """Get the sum of num1 and num2, then multiply that sum by num3"""

    return (num1 + num2) * num3


def add_cubes(num1, num2):
    """add the cubes of num1 and num2"""

    return (num1 ** 3) + (num2 ** 3)

