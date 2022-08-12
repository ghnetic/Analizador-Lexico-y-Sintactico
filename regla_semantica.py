#importar biblioteca
from lark import Transformer, v_args


@v_args(inline=True)
class ReglaSemantica(Transformer):
    def __init__(self):
        self.var = {}
    
    def sumar(self, valor1, valor2):
        return float(valor1) + float(valor2)

    def restar(self, valor1, valor2):
        return float(valor1) - float(valor2)