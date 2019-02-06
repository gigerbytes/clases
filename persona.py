#Crear una carpeta que se llame clases y adentro poner los$
# archivos dino.py persona.py

# Crear una clase Persona() que tenga como atributos nombre, edad 
# y profesion. Al instanciar la clase tiene que saludar igual que el
# dino diciendo sus atributos

class Persona:
    def __init__(self,un_nombre="",una_edad="",una_profesion=""):
        self.nombre = un_nombre
        self.edad = una_edad
        self.profesion = una_profesion
        print("Hola mi nombre es", un_nombre, "tengo", una_edad, "anhos y soy", una_profesion)

student= Persona("Anonimo",22,"futbolista")