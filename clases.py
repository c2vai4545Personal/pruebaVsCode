class Persona():
    def __init__(self):
        self.raza = humano
        self.idiomas = ["español"]

    def setNombre(self, nomb):
        self.nombre = nomb

    def setApellido(self, ape):
        self.apellido = ape

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def hablar(dialogo):
        print(dialogo)

    def caminar(self):
        return "estoy caminando"

class Informatico(Persona):
    def __init__(super):
        self.lenguajes = []

    def setLenguaje(self, lenguaje):
        self.lenguajes.append(lenguaje)

    def getLenguajes(self):
        return self.lenguajes
    
class BackEndDev(Informatico):
    def __init__(super):
        self.frameworks = []

    def getFrameworks(self):
        return self.frameworks
    
    def setFrameworks(self, framework):
        self.frameworks.append(framework)

    def programar(self):
        return """Compilando\n
        ...\n
        Compilado con exito
        """


class Support(Informatico):
    def __init__(super):
        self.os = []

    def getOs(self):
        return self.os
    
    def setOs(self, newOs):
        self.os.append(newOs)

    def repararServer(self):
        return 'Realizando Reparacion'
