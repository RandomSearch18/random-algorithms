import sys

sys.setrecursionlimit(10_000)
sys.set_int_max_str_digits(100_000)


def factorial(num: int):
    """Calculates the factorial of a number, without using math.factorial()"""
    if num == 0:
        return 1
    if num < 0:
        raise ValueError("Factorial of a negative number is not defined")

    return num * factorial(num - 1)


print(factorial(1000))
