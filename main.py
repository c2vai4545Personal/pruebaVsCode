from clases import *

carlos = BackendDev()
carlos.setNombre("Carlos")
carlos.setApellido("Nuñez")
carlos.setLenguaje('Python 3')
carlos.setFramework("Flask")

print(f'Hola, mi nombre es {carlos.getNombre()} {carlos.getApellido()} y mis lenguajes son estos: ')
for lenguaje in carlos.getLenguajes():
    print(lenguaje)
    