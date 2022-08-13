#importar biblioteca
from lark import Transformer, v_args
import re

@v_args(inline=True)
class ReglaSemantica(Transformer):
    def __init__(self):
        self.var = {}
    
    #Funcion para la operacion Sumar
    def sumar(self, valor1, valor2):
        return float(valor1) + float(valor2)

    #Funcion para la operacion Restar
    def restar(self, valor1, valor2):
        return float(valor1) - float(valor2)

    #Funcion para la operacion Concatenar
    def concatenar(self,valor1, valor2):
        return (self.LimpiarParam(self.var[valor1]) + " " + self.LimpiarParam(self.var[valor2]))

    def concatenacion(self, valor1, valor2):
        return self.LimpiarParam(self.var[valor1]) + " " + valor2
    
    #Funcion para la operacion repeticion 
    def repeticion(self, num, palabra):
        return int(num) * self.LimpiarParam(palabra)
        
    #Funciones para las operaciones de imprimir    
    def imprimiroperacion(self, cadena):
        print ("%s" % cadena)

    def obtenervariable(self, variable):
        return self.var[variable]

    def imprimirvariable(self, variable):
        print ("%s" % self.obtenervariable(variable))

    def imprimir(self, parametro):
        print ("%s" % self.LimpiarParam(parametro))

    def imprimiroperacion(self, operacion):
        print ("%s" % operacion)

   #Funcion para Limpiar Parametro
    def LimpiarParam(self, parametro):
        if re.match(r"^\'[^\']*\'$", parametro):
            return parametro[1:-1]
        else:
            return parametro

    #Funcion para asignar valor 
    def asignacion(self, variable, valor):
        self.var[variable] = valor