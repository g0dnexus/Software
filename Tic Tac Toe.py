def run_program():
    while True:
        text = input("Enter the text / Введите текст: ")
        count = int(input("Enter the number of repetitions / Введите количество повторений: "))

        prompt = "Choose the function / Выберите функцию:\n1. In line / В строчку\n2. In a column with numbering / В столбик с нумерацией\n3. In a column without numbering / В столбик без нумерации\n"

        while True:
            choice = input(prompt)

            if choice == "1":
                result = text * count
                print("In line / В строчку:")
                print(result)
                break
            elif choice == "2":
                print("In a column with numbering / В столбик с нумерацией:")
                for i in range(1, count + 1):
                    print(f"{i}. {text}")
                break
            elif choice == "3":
                print("In a column without numbering / В столбик без нумерации:")
                for i in range(count):
                    print(text)
                break
            else:
                print("Invalid choice / Неверный выбор")

        end_program = input("Do you want to end the program? (yes/no) / Хотите завершить программу? (да/нет): ")
        if end_program.lower() == "yes" or end_program.lower() == "да":
            break

run_program()
