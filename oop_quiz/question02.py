class Pizza:
    _counter = 0

    def __init__(self, ingredients):
        Pizza._counter += 1
        self.ingredients = ingredients
        self.order_number = Pizza._counter

    @staticmethod
    def hawaiian():
        return Pizza(["ham", "pineapple"])

    @staticmethod
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])


p1 = Pizza(["bacon", "parmesan", "ham"])
p2 = Pizza.garden_feast()

print(p1.ingredients)
print(p1.order_number)
print(p2.ingredients)
print(p2.order_number)
