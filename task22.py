
def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    groups = {}

    for student in students:
        if student["group"] not in groups:
            groups[student["group"]] = []

        groups[student["group"]].append(student["name"])

    return groups

students = [
    {"name": "Alice", "group": "A"},
    {"name": "Bob", "group": "B"},  
    {"name": "Charlie", "group": "A"},
    {"name": "David", "group": "B"},
    {"name": "Eve", "group": "C"}
]

result = group_students(students)
print(result)