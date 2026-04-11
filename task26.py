def merge_dicts(a: dict, b: dict) -> dict:
    if a == b:
        return b
    
    a.update(b)
    return a

a = {"name": "Alice", "age": 30}
b = {"name": "Alice", "age": 30}

result = merge_dicts(a, b)
print(result)