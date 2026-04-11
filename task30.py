def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}

    for key, value in d.items():
        if value != 0:
            result[key] = value

    return result

data = {
    "a": 1,
    "b": 0,
    "c": 3
}

filtered_data = filter_non_zero(data)
print(filtered_data)