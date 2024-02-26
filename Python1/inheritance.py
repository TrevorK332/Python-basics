class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Receptionist(Employees):
    def __init__(self, name, salary, gender):
        super().__init__(name, salary)
        self.gender = gender
class Front_end:
    def __int__(self,JAVA,CSS,HTML):

obj1 = Receptionist('Susan Smith', 150000, 'Female')
obj2 = Employees('Trevor Kimani', 150000)

print(obj1.name)
print(obj2.name)
