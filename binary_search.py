def binary_search_part(array: list[float], target_item: float,
                       start_index: int, end_index: int):
    """Finds the index of the provided item in a section of the provided ordered list"""
    NOT_FOUND = -1

    if start_index >= end_index:
        return NOT_FOUND

    relavant_part = array[start_index:end_index]
    midpoint = (len(relavant_part) - 1) // 2
    original_midpoint = start_index + midpoint  # index of our midpoint, in the original array
    #print(relavant_part, midpoint)
    middle_item = relavant_part[midpoint]

    if middle_item == target_item:
        return original_midpoint
    if target_item < middle_item:
        return binary_search_part(array, target_item, start_index,
                                  original_midpoint)
    if middle_item < target_item:
        return binary_search_part(array, target_item, original_midpoint + 1,
                                  end_index)


def binary_search(array: list[float], target_item: float):
    """Finds the index of the provided number in the provided ordered list of numbers"""
    start = 0
    end = len(array)
    return binary_search_part(array, target_item, start, end)


if __name__ == "__main__":
    import math

    demo_array = [
        -math.inf, -100, -2, math.pi, 2 * math.pi, 81, 300, 360, 365, 366,
        1984, 6.022e23, math.inf
    ]
    print(demo_array)
    print(f"81 is at index {binary_search(demo_array, 81)}")
    print(
        f"Avogadro's constant is at index {binary_search(demo_array, 6.022e23)}"
    )
    print(f"Tau (τ) is at index {binary_search(demo_array, math.tau)}")
    print(f"-∞ is at index {binary_search(demo_array, -math.inf)}")
    print(f"365.25 is at index {binary_search(demo_array, 365.25)}")
