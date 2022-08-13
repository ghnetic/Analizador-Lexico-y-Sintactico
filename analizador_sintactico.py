from regla_semantica import *
from regla_gramatica import *
from lark import Lark, Transformer

class Analizador_Sintactico:
    def __init__(self, text):
        self.text=text
    
    def compilar(self):
        parser= Lark(gramatica, parser="lalr", transformer=ReglaSemantica())
        lenguaje=parser.parse
        entrada=self.text

        try:
            lenguaje(entrada)
        except Exception as error:
            print("Errorsito: %s" % error)