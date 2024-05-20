def merge_lists(list_a, list_b):
    """Merges two sorted lists into one sorted list"""
    result = []
    position_a = 0
    position_b = 0
    while position_a < len(list_a) and position_b < len(list_b):
        item_a = list_a[position_a]
        item_b = list_b[position_b]
        if item_b < item_a:
            result.append(item_b)
            position_b += 1
        else:
            result.append(item_a)
            position_a += 1

    result.extend(list_a[position_a:])
    result.extend(list_b[position_b:])
    print(f"Merged {list_a} + {list_b} into", result)
    return result


def split_list(array):
    """Splits a list in half"""
    midpoint = len(array) // 2
    left_half = array[:midpoint]
    right_half = array[midpoint:]
    return (left_half, right_half)


# print(split_array([0,1,2,3,4,5]))
# print(split_array([0,1,2,3,4]))
# print(merge_lists([5, 6], [0, 1]))


def merge_sort(array):
    if len(array) == 1:
        return array
    if len(array) == 0:
        return []
    a, b = split_list(array)
    print(f"Splitting {array} into", a, b)
    return merge_lists(merge_sort(a), merge_sort(b))


print("Result:", merge_sort([8, 3, 0, -30]))
