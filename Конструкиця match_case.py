cmd = 11

match cmd:
    #case str(): #проверка что переменная cmd является строкой
    case str() as command: # проверка cmd является строкой если это так создается переменная command которая ссылается на top
        print(f"строковая команда {command}")
    case bool() as command:  # проверка cmd является строкой если это так создается переменная command которая ссылается на top
        print(f"булевая команда {command}")
    case int() | float() as command if 0<= command <= 10:  # проверка cmd является строкой если это так создается переменная command которая ссылается на top
        print(f"команда {command}")
    case _:
        print("другое")


"""cmd = 'right'

match cmd:
    case command:
        print(f"команда: {command}")
        #Переменная command шаблона case не делет никаких проверок ссылается на константу cmd
        #command = cmd. Блок отработает всегда так как не делает никаких проверок


#print("проверки завершены")"""

"""cmd = 'right'

match cmd:
    case "top":
        print("вверх")
    case "left":
        print("влево")
    case "right":
        print("право")
    case _:
        print("другое")

print("проверки завершены")

"""
