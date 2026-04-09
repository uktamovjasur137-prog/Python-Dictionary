scores = {
    "math": 90,
    "english": 85,
    "science": 92
}
count = 0
for subject, score in scores.items():
    if type(score) == int:
        count += score

print(count)