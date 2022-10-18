class Cliente:

    def __init__(self, dpi, nombre, edad, nit):
        self.dpi = dpi
        self.nombre = nombre
        self.edad = edad
        self.nit = nit


    #MÉTODOS GET
    def getDpi(self):
        return self.dpi
    
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getNit(self):
        return self.nit

    #MÉTODOS SET
    def setDpi(self, dpi):
        self.dpi = dpi
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setEdad(self, edad):
        self.edad = edad
    
    def setNit(self, nit):
        self.nit = nit
