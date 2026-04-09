book = {
    "title": "Python Basics",
    "author": "Diyorbek Jumanov",
    "pages": 250
}

key = input("Soz kiriting: ")

result = book.get(key, "Topilmadi")
print(result)