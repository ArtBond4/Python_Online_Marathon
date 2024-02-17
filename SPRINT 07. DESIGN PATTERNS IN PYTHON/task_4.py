class Washing:
    # Subsystem # 1
    def wash(self):
        print("Washing...")

class Rinsing:
    # Subsystem # 2
    def rinse(self):
        print("Rinsing...")

class Spinning:
    # Subsystem # 3
    def spin(self):
        print("Spinning...")

class WashingMachine:
    def __init__(self):
        self.Washing = Washing()
        self.Rinsing = Rinsing()
        self.Spinning = Spinning()

    def startWashing(self):
        self.Washing.wash()
        self.Rinsing.rinse()
        self.Spinning.spin()
