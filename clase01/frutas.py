class Fruta(object):
    # conviene poner de forma explicita object

    #def __init__(self, color, peso, tipo, nombre):
    def __init__(self, *args, **kwargs):
        color, peso, tipo, nombre = args[:5]
        # __ para metodos magicos
        self.color = color
        self.peso = peso
        self.tipo = tipo
        self.nombre = nombre
    
    def get_info(self):
        #return f"{self.nombre} color: {self.color}" # anda para python 3.7
        return self.nombre + " " + str(self.tipo)

class Banana(Fruta):

    def __init__(self, peso):
        super(Banana, self).__self__("amarillo", peso, "tipo", "banana")

# MRO python, orden en python para multiple herencia

if __name__ == "__main__":
    print "manzana"

    canasta = [
        Fruta("amarillo", 10, "tipo", "banana")
    ]

    print canasta[0].get_info()