
class Arle:
    def __init__(self,name):
        self.name=name
    def save(self):
        print(f"I save you {self.name}")

class Raiden(Arle):
    def fall(self):
        print("you falling!!")

class Furina(Arle):
    def not_fall(self):
        print("YOU not falling!!")

class Nahida(Raiden):
    def name(self):
        print("IM Nahida!")

class Ei(Furina):
    def name(self):
        print("HII im Ei!")

class Shogun(Raiden,Furina):
    def name(self):
        print("Hii im shogun!!")

arle=Arle("Arlecchino")
raiden=Raiden("Raiden")
furina=Furina("Furina")
nahida=Nahida("Nahida")
shogun=Shogun("Shogun")
ei=Ei('Ei')

shogun.save()
shogun.fall()