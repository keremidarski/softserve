class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("Spinning...")


class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.washing.wash()
        self.rinsing = Rinsing()
        self.rinsing.rinse()
        self.spinning = Spinning()
        self.spinning.spin()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()
