freq = {}

while True:
    text = input("Введите текст (для выхода введите q): ")
    if text == "q":
        break
    for char in text:
        if char.isalpha() or char.isdigit():
            freq[char] = freq.get(char, 0) + 1
    for char, count in freq.items():
        print(f"{char} - {count}")
