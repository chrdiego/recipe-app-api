def add(x, y):
    return x + y
    

class Perro:
    color = "Negro"

    def __init__(self):
        self.color = "negro"
        self.prueba = "123"
        print(f"Se creo un perro {self.color}")

    def ladrar(self, volumen="ruidoso"):
        print(f"el perro ladra de una manera {volumen}")


perro = Perro()
# print(f"perro color: {perro.color}")
print(perro.prueba)