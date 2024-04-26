class Person:
    # name = 'Ivan'
    # age = 10

    def set(self, name, age):
        self.name = name
        self.age = age

vlad = Person() # влад объект класса person
vlad.set("Влад", 25)
print(vlad.name + " " + str(vlad.age))


# vlad.name = 'Vlad'
# print(vlad.name)
#
# ivan = Person() # влад объект класса person
#
# print(ivan.name)

class Car:
    def set(self, brend, class_auto, country):
        self.brend = brend
        self.clas_auto = class_auto
        self.country = country

car1 = Car()
car1.set("Тойота", "Купе", "Япония")
print(car1.brend, car1.country)
