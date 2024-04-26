try:
    file = open("my_file.txt", encoding='utf-8')
    try:
        s = file.readlines()
        int(s)
        print(s)
    finally:
        file.close()
except FileNotFoundError:
    print("файл невозможно найти так как он не найден")
except:
    print("ошибка при работе с файлом")




"""Замена блока try finally файловым менеджером контекста"""
try:
    with open("my_file.txt", encoding='utf-8') as file:
        s = file.readlines()
        print(s)
except FileNotFoundError:
    print("файл невозможно найти так как он не найден")
except:
    print("ошибка при работе с файлом")
finally:
    print(file.closed)