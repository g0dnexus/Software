text = input("Enter the text / Введите текст: ")
count = int(input("Enter the number of repetitions / Введите количество повторений: "))

prompt = "Choose the function / Выберите функцию:\n1. In line / В строчку\n2. In a column with numbering / В столбик с нумерацией\n3. In a column without numbering / В столбик без нумерации\n"

choice = input(prompt)

if choice == "1":
    # In line / В строчку
    result = text * count
    print("In line / В строчку:")
    print(result)
elif choice == "2":
    # In a column with numbering / В столбик с нумерацией
    print("In a column with numbering / В столбик с нумерацией:")
    for i in range(1, count + 1):
        print(f"{i}. {text}")
elif choice == "3":
    # In a column without numbering / В столбик без нумерации
    print("In a column without numbering / В столбик без нумерации:")
    for i in range(count):
        print(text)
else:
    # Invalid choice / Неверный выбор
    print("Invalid choice / Неверный выбор")
