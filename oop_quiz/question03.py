class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(string):
        parsed = string.split("-")

        return Employee(parsed[0], parsed[1], int(parsed[2]))


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.firstname)
print(emp1.lastname)
print(emp1.salary)
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)
