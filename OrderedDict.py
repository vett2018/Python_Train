from collections import OrderedDict
import json

if __name__ == '__main__':

    d = OrderedDict()

    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 333
    d['grok'] = 4

    print(f' 1 простой вывод словаря: {d}')
    print("----------------------------------------")
    for key in d:
        print(key, d[key])
        #print(f' 2 вывод ключ и значение {key, d[key]}')
    print("----------------------------------------")

    json_dict = json.dumps(d) #серилизация в JSON
    print(json_dict)