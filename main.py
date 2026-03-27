
# clase persona tiene que ser en mayuscula y con la palabra reservada class




class Persona:
    def __init__(self, nombre,edad): #este es el constructor
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"hola mi nombre es: {self.nombre} y tengo {self.edad}") #esto ya es un método que se aplica a una instancia

    def cumplir_anios(self):
        self.edad += 1




# instancia
juanito = Persona("juanito", 34)
carlos = Persona("carlos", 32)

print(juanito.cumplir_anios())




