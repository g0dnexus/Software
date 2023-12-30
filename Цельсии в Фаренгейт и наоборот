def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("1. Перевести градусы Цельсия в градусы Фаренгейта")
print("2. Перевести градусы Фаренгейта в градусы Цельсия")
choice = int(input("Выберите опцию (1 или 2): "))

if choice == 1:
    celsius = float(input("Введите градусы Цельсия: "))
    result = c_to_f(celsius)
    print("{} градусов Цельсия = {} градусов Фаренгейта".format(celsius, result))
elif choice == 2:
    fahrenheit = float(input("Введите градусы Фаренгейта: "))
    result = f_to_c(fahrenheit)
    print("{} градусов Фаренгейта = {} градусов Цельсия".format(fahrenheit, result))
else:
    print("Неверно выбрана опция. Пожалуйста, выберите 1 или 2.")
