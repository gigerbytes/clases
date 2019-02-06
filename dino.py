
# Agregarle una propiedad color a la clase Dino, y que salude 
# diciendo su nombre y de que color es el dinosaurio

#Crear una carpeta que se llame clases y adentro poner los$
# archivos dino.py persona.py

# Crear una clase Persona() en el archivo persona.py que tenga como atributos 
# nombre, edad y profesion.
# Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos


class Dino:
    # cola, dientes, color, size
    def __init__(self,un_nombre="", un_color="verde"):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy un dinosaurio, me llamo ", self.nombre, "y soy ", self.color)

#Aca instanciamos varios objetos del tipo Dino
pepito = Dino("Pepe", "Verde")
pepita = Dino("Pepa", "plata")
pepite = Dino("Pepx")
pepiti = Dino("Pxpx", "Azulgrana")
pepo = Dino(un_color="Pink", un_nombre="GGGG")