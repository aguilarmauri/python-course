class Libro(object):
    def __init__(self, fecha, isbn, editorial, titulo, paginas, precio, autores:list):
        self.fecha = fecha
        self.isbn = isbn
        self.editorial = editorial
        self.titulo = titulo
        self.paginas = paginas
        self.precio = precio
        self.autores = autores

    def agregar_autor(self, autor):
        self.autores.append(autor)

class Autor(object):
    def __init__(self, nombre, apellido, dni, nacionalidad, libros:list):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nacionalidad = nacionalidad
        self.libros = libros
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def __str__(self):
        return "info del objeto"
    #print del objeto



if __name__ == "__main__":
    

    autor1 = Autor("Oscar", "Wilde", 7442345, "Irlandes")

    autor1.agregar_libro(
        Libro("1/1/1890", "123", "Mamo", "Dorian Grey", "Oscar", 260, 300)
    )


# @staticmethod
# @classmethod