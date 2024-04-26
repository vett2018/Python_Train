class Person:
    name = 'Ivan'
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1 # по умолчанию на первом курсе

igor = Student()
igor.set('Igor', 19)
igor.course = 2
print(igor.course)

vlad = Person() # влад объект класса person
vlad.set("Влад", 25)
print(vlad.name + " " + str(vlad.age))

ivan = Person()
ivan.set('Иван', 56)
print(ivan.age)