class Animal():
    def __init__(self, name):
        self.animalname = name
    def speak(self):
        print(self.animalname)

class Dog(Animal):
    pass
d1 = Dog("Chiku")
d1.speak()
