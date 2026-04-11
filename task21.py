names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
def count_names(names: list[str]) -> dict[str, int]:
    result = {}
    for name in names:
        count = names.count(name)

        result[name] = count
    return result

result = count_names(names)
print(result)