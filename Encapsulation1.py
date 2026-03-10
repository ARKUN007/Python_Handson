class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private property is age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
p1 = Person("Avinash", 29)
print(p1.name)
#print(p1.age) this line will throw error because we have set age as provate

print(p1.get_age()) # so we have to call get_age() to see the age

p1.set_age(30) #changing the age with set_age() method
print(p1.get_age()) #now it will print new age