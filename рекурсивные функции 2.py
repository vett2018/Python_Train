"""Обход псевдо-файловой системы в виде словаря"""
F = {
    'C:\\': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    },
    'D:\\': {
        'OS': {
            'VM-Ubuntu-18.04.4': ['mksSandbox-0.log','mksSandbox-2.log','mksSandbox-3.log']
        },
        'Math': ['aids-vaccine-2.pdf', 'beekeeping-1.pdf', 'rabbit-husbandry-2.pdf']
    }
}

def get_files(path, depth=0):
    """
    Функция обхода словаря псевдо-файловой системы
    :param path: ссылка на словарь (фактический параметр)
    :param depth: глубина обхода (формальный параметр) равна нулю по умолчанию
    :return:
    """
    for key_ in path: #перебор словаря по ключам

        print(" "*depth, key_) #вывод ключей
        if type(path[key_]) == dict: #если ключ является словарем, то по рикурсии обходим его вызывая функцию (рекурсивно)
            get_files(path[key_], depth+1) #повтор рекурсии и изменена глубина
        else:
            print(" "*(depth+1), " ".join(path[key_])) #выводим список из отдельных файлов, второй аргумент обьединение строк из этого списка


get_files(F)