class Person():
    def __init__(self, fname, lname):
        self.firstname =fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
p1 = Person("Avinash", "Kumar")
p1.printname()

# Below is the child class inheriting the Person class property
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "graduated in ", self.graduationyear)
s1 = Student("Avinash", "Kumar", 2020)
s1.welcome()