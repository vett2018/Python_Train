def say_name(name): #внешняя функция
    def say_goodbye(): #внутрення функция
        # nonlocal name # - равносильно
        print("don't say me goodbye, " + name + "!")

    #say_goodbye() #вызываем внутренюю функцию из внешней
    return say_goodbye #внешняя функция возвращают ссылку на внутренню функцию


#say_name("Sergey")

f = say_name("Sergey") #сохраняем ссылку на внутренюю функцию
f()
f2 = say_name("Alex")
f2()

"""Функция счетчик. При каждом вызове этой функции ее значение увеличивается на еденицу"""
def counter(start = 0):
    ''' Внешняя функция с начальным значение
    :param start: начальное значение
    :return: возвращает внутренюю функцию
    '''
    def step():
        '''
        Внктренняя функция принимает значение start и увеличивает его
        :return:
        '''
        nonlocal start #переменная из внешнего окружения
        start +=1
        return start

    return step #возвращает ссылку на функцию step



"""Два счетчика которые работают независимо друг от друга"""
c1 = counter(10)
c2 = counter(10)
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())

"""Функция удаление неныжных символов в начале и конце строки"""
def strip_string(strip_chars = " "):
    """Функция по умолчанию имеет параметр которая содержит пустой пробел"""
    def do_strip(string):
        """
        Функция содержит параметр это та строка из которой нужно удалить символы
        :param string:  та строка из которой удаляем символы
        :return:
        """
        return string.strip(strip_chars) #удаляет символы вначале и в конце

    return do_strip #внешняя функция возвращает внутреннюю функцию

strip1 = strip_string(" !?,.;") #вызов внешней функции и присваиваем strip1 ссылку на вызов функции

#вызов внутренней функции do_strip через ссылку strip1

print(strip1(" !!!? hello python !"))
