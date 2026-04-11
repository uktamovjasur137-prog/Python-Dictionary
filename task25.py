def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    groups = {}
    for person in people:
        age = person["age"]
        name = person["name"]

        groups.setdefault(age, []).append(name)
    return groups


people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
]

result = group_by_age(people)
print(result)