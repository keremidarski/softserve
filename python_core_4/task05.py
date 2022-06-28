class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"


p1 = Player("David Jones", 25, 175, 75)

print(p1.get_age() == "David Jones is age 25")
print(p1.get_height() == "David Jones is 175cm")
print(p1.get_weight() == "David Jones weighs 75kg")
