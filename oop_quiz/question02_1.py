class Pizza:
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    hawaiian = classmethod(lambda cls: cls(["ham", "pineapple"]))

    @classmethod
    def meat_festival(cls):
        return cls("beef, meatball, bacon".split(", "))

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])

    """
	@property
	def hawaiian(self):
		return self.ingredients
	@property
	def meat_festival(self):
		return self.ingredients
	@property
	def garden_feast(self):
		return self.ingredients
	@hawaiian.setter
	def hawaiian(self):
		self.ingredients = ['ham', 'pineapple']
	@meat_festival.setter
	def meat_festival(self):
		self.ingredients = ['beef', 'meatball', 'bacon']
	@garden_feast.setter
	def garden_feast(self):
		self.ingredients = ['spinach', 'olives', 'mushroom']
"""


p1 = Pizza(["bacon", "parmesan", "ham"])
p2 = Pizza.garden_feast()

print(p1.ingredients)
print(p1.order_number)
print(p2.order_number)
print(p2.ingredients)
