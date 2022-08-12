#importar biblioteca
from lark import Transformer, v_args


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
        return (self.cleanParam(self.var[valor1]) + " " + self.cleanParam(self.var[valor2]))

    def concatenacion(self, valor1, valor2):
        return self.cleanParam(self.var[valor1]) + " " + valor2
    
    #Funcion para la operacion repeticion 
    def repeticion(self, num, palabra):
        return int(num) * self.cleanParam(palabra)
 