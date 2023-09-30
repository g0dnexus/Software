import random

def guess_number(start, end):
    secret_number = random.randint(start, end)
    attempts = 0  # количество попыток

    while True:
        try:
            guess = int(input(f"Guess the number between {start} and {end} / Угадайте число между {start} и {end}: "))
            attempts += 1

            if guess < secret_number:
                print("The hidden number is bigger / Загаданное число больше.")
            elif guess > secret_number:
                print("The hidden number is less / Загаданное число меньше.")
            else:
                print("Congratulations, you guessed the number! / Поздравляю, вы угадали число!")
                print(f"Number of attempts: {attempts} / Количество попыток: {attempts}")
                break
        except ValueError:
            print("Error: Enter an integer / Ошибка: введите целое число.")

def play_game():
    while True:
        try:
            start = int(input("Select the initial number in the range / Выберите начальное число в диапазоне: "))
            end = int(input("Select a finite number in the range / Выберите конечное число в диапазоне: "))
            if start >= end:
                print("Error: the initial number must be less than the final number / Ошибка: начальное число должно быть меньше конечного числа.")
            else:
                break
        except ValueError:
            print("Error: Enter an integer / Ошибка: введите целое число.")
            
    guess_number(start, end)

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no) / Хотите сыграть еще раз? (да/нет): ")
        if choice.lower() == "yes" or choice.lower() == "да":
            return True
        elif choice.lower() == "no" or choice.lower() == "нет":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'. / Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")

while True:
    play_game()
    if not play_again():
        break
