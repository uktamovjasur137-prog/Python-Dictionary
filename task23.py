def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    groups = {}

    for index, number in enumerate(numbers):
        groups.setdefault(number, []).append(index)
    
    return groups
    
numbers = [1, 2, 3, 2, 1, 4]
result = group_indices(numbers)
print(result)