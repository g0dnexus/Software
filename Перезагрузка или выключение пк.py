import os

def reboot_pc():
    if os.name == 'nt':
        os.system('shutdown /r /t 0')
    elif os.name == 'posix':
        os.system('reboot')
    else:
        print('Не удалось распознать операционную систему.')

def shutdown_pc():
    if os.name == 'nt':
        os.system('shutdown /s /t 0')
    elif os.name == 'posix': 
        os.system('shutdown now')
    else:
        print('Не удалось распознать операционную систему.')

while True:
    print("Выберите действие:")
    print("1. Перезагрузить ПК")
    print("2. Выключить ПК")
    choice = input("Введите номер выбранного действия: ")

    if choice == "1":
        reboot_pc()
    elif choice == "2":
        shutdown_pc()
    else:
        print("Неверный ввод. Пожалуйста, выберите 1 или 2.")
