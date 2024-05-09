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
    extra_items_a = len(list_a) - len(list_b)
    if extra_items_a > 0:
        extra_items = list_a[-extra_items_a:]
        result += extra_items
    elif extra_items_a < 0:
        extra_items = list_b[extra_items_a:]
        result += extra_items
    return result

print(merge_lists([3, 6, 9, 21], [2, 4, 8, 100]))
print(merge_lists([3, 6, 9, 21], [2, 4, 8, 100, 200, 3400]))