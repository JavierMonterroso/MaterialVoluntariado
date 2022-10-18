class Usuario:

    def __init__(self, dpi, nombre, edad):
        self.dpi = dpi
        self.nombre = nombre
        self.edad = edad

    def getDpi(self):
        return self.dpi

    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad

    def setDpi(self, dpi):
        self.edad = dpi
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad
