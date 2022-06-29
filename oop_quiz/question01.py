class Employee:
    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        self.__dict__.update(kwargs)
        self.get_names(self.full_name)

    def get_names(self, full_name):
        list_name = full_name.split(" ")
        self.name = list_name[0]
        self.lastname = list_name[1]


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee(
    "Giancarlo Rossi", salary=115000, height=182, nationality="Italian"
)
print(richard.height)
print(giancarlo.nationality)
