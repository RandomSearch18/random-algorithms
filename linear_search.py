def linear_search(names: list[str], target_name: str):
    result_index = -1
    found = False
    i = 0
    while i < len(names) and not found:
        if names[i] == target_name:
            result_index = i
            found = True
        i = i + 1

    return result_index


demo_names = ["Andrew", "Mish", "Dan"]

target_name = "Mish"
found_index = linear_search(demo_names, target_name)
print(f"Found {target_name} at index {found_index}")
