class OnesThreesNines:
    def __init__(self, number):
        self.number = number
        self.nines = number // 9
        self.threes = number // 3
        self.ones = number 


n1 = OnesThreesNines(5)
print(n1.nines == 0)
print(n1.ones == 5)
print(n1.threes == 1)