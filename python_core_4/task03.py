class Person:
    def __init__(self, name, liked_foods, hated_foods):
        self.name = name
        self.liked_foods = liked_foods
        self.hated_foods = hated_foods

    def taste(self, food_name):
        if food_name in self.liked_foods:
            return f"{self.name} eats the {food_name} and loves it!"
        elif food_name in self.hated_foods:
            return f"{self.name} eats the {food_name} and hates it!"
        else:
            return f"{self.name} eats the {food_name}!"


p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))