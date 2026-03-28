
#Pilares de la poo


#ENCAPSULACION

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo #se puede encapsular con __ (2 guiones bajo) para ocultar métodos o atributos

    def __str__(self):
        return f"esto es el objeto: {self.titular} y tiene un saldo de: {self.saldo}"

    def Depositar(self, monto): 
        if monto > 0:
            self.__saldo += monto

    def Retirar(self, monto):
        if monto < self.__saldo:
            self.__saldo -= monto

cuenta1 = CuentaBancaria("juanito", 10000)
cuenta2 = CuentaBancaria("marcela",100)

#eso es el objeto <__main__.CuentaBancaria object at 0x729a677a82f0>
#print(cuenta1.retirar(1000))
#print(cuenta1)



#HERENCIA

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def moverse(self):
        print("auto se movio!!")


class Auto(Vehiculo):
    def moverse(self):
        print("auto moviendose")



class Moto(Vehiculo):
    def moverse(self):
        print("moto moviendose")

auto = Auto(byd)
moto = Moto(ktm)

auto.moverse()
moto.moverse()

