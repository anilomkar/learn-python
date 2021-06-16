class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


employee = Employee("Anil", 40)

print(employee.name)
print(employee.age)

print(employee.getAge())
print(employee.getName())