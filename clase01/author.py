
class Autor(object):

    def __init__(self, nombre, apellido, dni, nacionalidad, libros: list):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nacionalidad = nacionalidad
        assert type(libros) == list
        self.libros = libros

    def get_nombre_completo(self):
        return f"{self.nombre}, {self.apellido}"

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def __str__(self):
        return f"Autor {self.nombre}, {self.apellido} tiene {len(self.libros)} libros."

