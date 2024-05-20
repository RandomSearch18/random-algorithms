def fib(n: int):
    """Returns the Fibonacci sequence up to n, using interation"""
    if n < 0:
        raise ValueError(
            "Fibonacci sequence does not exist for negative numbers")

    sequence = [0, 1]  # Start with 0 and 1
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def generate_fibonacci_number(n: int):
    """Returns the nth number in the Fibonacci sequence, using recursion"""
    if n <= 1:
        return 1
    else:
        return generate_fibonacci_number(n - 2) + generate_fibonacci_number(n -
                                                                            1)

print(generate_fibonacci_number(7))  # 21
