def sum_of_even_numbers(limit: int, start=0):
    """Generates the sum of all even numbers between 0 and limit="""
    if limit == 0:
        # There's nothing below 0
        return 0

    return sum_of_even_numbers(limit - 2)


print(sum_of_even_numbers(8))
