def convert_length(value, unit):
    if unit in ["метры", "meters"]:
        meters = round(value, 4)
        kilometers = round(value / 1000, 4)
        centimeters = round(value * 100, 4)
        millimeters = round(value * 1000, 4)
        square_meters = round(value ** 2, 4)
        square_centimeters = round((value ** 2) * 10000, 4)

        return meters, kilometers, centimeters, millimeters, square_meters, square_centimeters
    elif unit in ["километры", "kilometers"]:
        kilometers = round(value, 4)
        meters = round(value * 1000, 4)
        centimeters = round(value * 100000, 4)
        millimeters = round(value * 1000000, 4)
        square_meters = round((value * 1000) ** 2, 4)
        square_centimeters = round(((value * 1000) ** 2) * 10000, 4)

        return meters, kilometers, centimeters, millimeters, square_meters, square_centimeters
    elif unit in ["сантиметры", "centimeters"]:
        centimeters = round(value, 4)
        meters = round(value / 100, 4)
        kilometers = round((value / 100) / 1000, 4)
        millimeters = round(value * 10, 4)
        square_meters = round((value / 100) ** 2, 4)
        square_centimeters = round(value ** 2, 4)

        return meters, kilometers, centimeters, millimeters, square_meters, square_centimeters
    elif unit in ["миллиметры", "millimeters"]:
        millimeters = round(value, 4)
        centimeters = round(value / 10, 4)
        meters = round((value / 1000), 4)
        kilometers = round(((value / 1000) / 1000), 4)
        square_meters = round(((value / 1000) ** 2), 4)
        square_centimeters = round(((value / 10) ** 2), 4)

        return meters, kilometers, centimeters, millimeters, square_meters, square_centimeters
    else:
        return None

def convert_time(value, unit):
    if unit in ["миллисекунды", "milliseconds"]:
        milliseconds = round(value, 4)
        seconds = round(value / 1000, 4)
        minutes = round((value / 1000) / 60, 4)
        hours = round(((value / 1000) / 60) / 60, 4)
        days = round((((value / 1000) / 60) / 60) / 24, 4)

        return milliseconds, seconds, minutes, hours, days
    elif unit in ["секунды", "seconds"]:
        seconds = round(value, 4)
        milliseconds = round(value * 1000, 4)
        minutes = round(value / 60, 4)
        hours = round((value / 60) / 60, 4)
        days = round(((value / 60) / 60) / 24, 4)

        return milliseconds, seconds, minutes, hours, days
    elif unit in ["минуты", "minutes"]:
        minutes = round(value, 4)
        seconds = round(value * 60, 4)
        milliseconds = round((value * 60) * 1000, 4)
        hours = round(value / 60, 4)
        days = round((value / 60) / 24, 4)

        return milliseconds, seconds, minutes, hours, days
    elif unit in ["часы", "hours"]:
        hours = round(value, 4)
        minutes = round(value * 60, 4)
        seconds = round((value * 60) * 60, 4)
        milliseconds = round(((value * 60) * 60) * 1000, 4)
        days = round((value * 60) / 24, 4)

        return milliseconds, seconds, minutes, hours, days
    elif unit in ["дни", "days"]:
        days = round(value, 4)
        hours = round(value * 24, 4)
        minutes = round((value * 24) * 60, 4)
        seconds = round(((value * 24) * 60) * 60, 4)
        milliseconds = round((((value * 24) * 60) * 60) * 1000, 4)

        return milliseconds, seconds, minutes, hours, days
    else:
        return None

while True:
    value = float(input("Enter value / Введите значение: "))
    unit = input("Enter unit of measurement (метры/meters, километры/kilometers, сантиметры/centimeters, миллиметры/millimeters, миллисекунды/milliseconds, секунды/seconds, минуты/minutes, часы/hours, дни/days): ")

    if unit in ["метры", "meters", "километры", "kilometers", "сантиметры", "centimeters", "миллиметры", "millimeters"]:
        meters, kilometers, centimeters, millimeters, square_meters, square_centimeters = convert_length(value, unit)

        print("Метры/Meters:", meters)
        print("Километры/Kilometers:", kilometers)
        print("Сантиметры/Centimeters:", centimeters)
        print("Миллиметры/Millimeters:", millimeters)
        print("Квадратные метры/Square Meters:", square_meters)
        print("Квадратные сантиметры/Square Centimeters:", square_centimeters)
    elif unit in ["миллисекунды", "milliseconds", "секунды", "seconds", "минуты", "minutes", "часы", "hours", "дни", "days"]:
        milliseconds, seconds, minutes, hours, days = convert_time(value, unit)

        print("Миллисекунды/Milliseconds:", milliseconds)
        print("Секунды/Seconds:", seconds)
        print("Минуты/Minutes:", minutes)
        print("Часы/Hours:", hours)
        print("Дни/Days:", days)

    choice = input("Would you like to continue? (yes/no) / Хотите продолжить? (да/нет): ")
    if choice.lower() != "yes" and choice.lower() != "да":
        break
