"""Передача произвольного количества позиционных аргументов *args
    Передача произвольного количества именованных аргументов"""
import xml.dom.minicompat


def os_path(disk, *args, sep='\\', **kwargs):
    """
    Фнкция для формирования маршрута к файлу,
на вход подается несколько строк, а на выходе формируется общий маршрут
    :param args: Произвольное число параметров
    :return:
    """
    #print(kwargs)#колекция dict
    #print(args) #колекция tuple
    args = (disk,) + args #добавление фактического параметра в коллекцию
    if 'trim' in kwargs and kwargs["trim"] == True:
    #проверка если ключ trim присутвует в коллекции и этот ключ (Trim) равен True то удаляем пробелы в начале и вконце
        args = [x.strip() for x in args]

    path = sep.join(args)
    return path

p = os_path("F:", "   ~stepik.org",
            "Добрый, добрый Python (Питон)",
            "39\\з39. Функция.docx",
            sep='/',trim=True)
print(p)

