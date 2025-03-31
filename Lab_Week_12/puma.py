from mammal import Mammal

class Puma(Mammal):
    def __init__(self, age, tick):
        super().__init__(age)
        self.tick = tick

    def speak(self):
        print("Roar! I'm a puma!")