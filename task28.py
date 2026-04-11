def group_by_length(words: list[str]) -> dict[int, list[str]]:
    groups = {}

    for word in words:
        length = len(word)

        groups.setdefault(length, []).append(word)

    return groups

words = ["apple", "banana", "cherry", "date", "fig", "grape"]
result = group_by_length(words)
print(result)