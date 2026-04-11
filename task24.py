def most_common_char(text: str) -> str:
    max_char = text[0]
    for char in text:
        if text.count(char) > text.count(max_char):
            max_char = char
    return max_char

text = input("Enter text: ")

result = most_common_char(text)
print(result)