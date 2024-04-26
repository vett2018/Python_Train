def add_value(value, lst=None):
    if lst is None: #if lst == None:
        lst = []

    lst.append(value)
    return lst

#l = add_value(1, [])
#l = add_value(2, [])
l = add_value(1)
print(l)
l = add_value(2)
print(l)