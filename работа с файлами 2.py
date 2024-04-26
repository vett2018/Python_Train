import pickle


# try:
#     with open("out.txt", 'a+') as file:
#         file.seek(0)
#         #file.write("Hello4")
#         file.writelines(["qwerty\n", "1234\n"])
#         s = file.readlines()
#         print(s)
# except:
#     print("ошибка при работе с файлом")

"""Сохранить коллекцию состоящую из книг в файл, а потом прочитать.
    Выполняется с помощью бинарного режима доступа.
    Сохранение произвольных данных в файл с помощю библиотеки pickle"""
# books = [
#     ("Евгений Онегин", "Пушкин А.С.", 200),
#     ("Муму", "Тургенев И.С.", 250),
#     ("Мастер и Маргарита", "Булгаков М.А", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# ]
# #file = open("out.bin", "wb") #открываем файл для чтения в бинарном виде
# #pickle.dump(books, file) # запись в бинарный файл
# file = open("out.bin", "rb")
# bs = pickle.load(file) # функция вохвращения колекции из бинарного файла
# file.close()
# print(bs)
# file.close()

"""Сохранение нескольких значений в бинарный файл"""
book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
book2 = ["Муму", "Тургенев И.С.", 250]
book3 = ["Мастер и Маргарита", "Булгаков М.А", 500]
book4 = ["Мертвые души", "Гоголь Н.В.", 190]

# try: #блок записи информации в бинарный файл
#     with open("out.bin", "wb") as file:
#         pickle.dump(book1, file)
#         pickle.dump(book2, file)
#         pickle.dump(book3, file)
#         pickle.dump(book4, file)
# except:
#     print("Ошибка при работе с файлом")

try: #блок чтения информации из бинарного файла
    with open("out.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except:
    print("Ошибка при работе с файлом")

print(b1, b2, b3, b4, sep='\n')


