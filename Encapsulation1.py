class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private property is age
    def get_age(self):
        return self.__age
p1 = Person("Avinash", 29)
print(p1.name)
#print(p1.age) this line will throw error because we have set age as provate

# so we have to call get_age() to see the age
print(p1.get_age())