class Person:
    name = 'Ivan'
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def set(self, name, age):
    #     self.name = name
    #     self.age = age

class Student(Person):
    course = 1 # по умолчанию на первом курсе
    def set(self, name, age):
        self.name = name
        self.age = age


igor = Student('Igor', 24)
print(igor.name + " "+ str(igor.age), igor.course)
igor.course = 5
print("Имя: ", igor.name, ", возраст - ", igor.age, ", курс - ", igor.course )

slava = Person('Slava', 25)
print("Имя =",slava.name, "Возраст =", slava.age)

# igor.set('Igor', 19)
# igor.course = 2
# print(igor.course)

# vlad = Person() # влад объект класса person
# vlad.set("Влад", 25)
# print(vlad.name + " " + str(vlad.age))

