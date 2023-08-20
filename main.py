class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self,color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color=color
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self,registro):
        self.registro=registro
    def asignarTipo(self,tipo):
        if tipo=="electrico" or tipo=="gasolina":
          self.tipo=tipo
class Auto:
    cantidadCreados=0
    def __init__(self,modelo, precio, asientos, marca, motor, registro):
        self.asientos=asientos
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = motor
        self.registro =registro
        
    def cantidadAsientos(self):
        a=0
        for i in self.asientos:
            if type(i)=="<class '__main__.Asiento'>":
                a+=1
        return a
    def verificarIntegridad(self):
        b=0
        for i in self.asientos:
            if i.registro!=self.registro!=self.motor.registro:
                b+=1
        if b>0:
            return "Las piezas no son originales"
        else:
            return "Auto original"