import datetime

date_format = "%d.%m.%Y"

while True:
    try:
        date1_str = input("Enter the first date in the format dd.mm.yyyy / Введите первую дату в формате дд.мм.гггг: ")
        date1 = datetime.datetime.strptime(date1_str, date_format).date()
        break
    except ValueError:
        print("Invalid date format! Try again. / Неверный формат даты! Попробуйте снова.")

while True:
    try:
        date2_str = input("Enter the second date in the format dd.mm.yyyy / Введите вторую дату в формате дд.мм.гггг: ")
        date2 = datetime.datetime.strptime(date2_str, date_format).date()
        break
    except ValueError:
        print("Invalid date format! Try again. / Неверный формат даты! Попробуйте снова.")


diff = date2 - date1
years = diff.days // 365
remaining_days = diff.days % 365

print(f"Difference between dates: {years} years {remaining_days} days / Разница между датами: {years} лет {remaining_days} дней")
print(f"Number of days / Количество дней:  {diff.days}")
print(f"Number of hours / Количество часов: {diff.days * 24}")
print(f"Number of minutes / Количество минут: {diff.days * 24 * 60}")
print(f"Number of seconds / Количество секунд: {diff.days * 24 * 60 * 60}")
print(f"Number of milliseconds / Количество миллисекунд: {diff.days * 24 * 60 * 60 * 1000}")

while True:
    choice = input("Do you want to know the difference between other dates? (yes/no) / Хотите узнать разницу между другими датами? (да/нет): ")
    if choice.lower() == "да" or choice.lower() == "yes":
        while True:
            try:
                date1_str = input("Enter the first date in the format dd.mm.yyyy / Введите первую дату в формате дд.мм.гггг: ")
                date1 = datetime.datetime.strptime(date1_str, date_format).date()
                break
            except ValueError:
                print("Invalid date format! Try again. / Неверный формат даты! Попробуйте снова.")

        while True:
            try:
                date2_str = input("Enter the second date in the format dd.mm.yyyy / Введите вторую дату в формате дд.мм.гггг: ")
                date2 = datetime.datetime.strptime(date2_str, date_format).date()
                break
            except ValueError:
                print("Invalid date format! Try again. / Неверный формат даты! Попробуйте снова.")


        diff = date2 - date1
        years = diff.days // 365
        remaining_days = diff.days % 365

  
        print(f"Difference between dates: {years} years {remaining_days} days / Разница между датами: {years} лет {remaining_days} дней")
        print(f"Number of days / Количество дней:  {diff.days}")
        print(f"Number of hours / Количество часов: {diff.days * 24}")
        print(f"Number of minutes / Количество минут: {diff.days * 24 * 60}")
        print(f"Number of seconds / Количество секунд: {diff.days * 24 * 60 * 60}")
        print(f"Number of milliseconds / Количество миллисекунд: {diff.days * 24 * 60 * 60 * 1000}")
    else:
        break
