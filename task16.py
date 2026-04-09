data = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent"
}

key = input("Kalit nomini kiriting: ")

if key in data:
    del data[key]
else:
    print("Bunday kalit yo‘q")

print(data)