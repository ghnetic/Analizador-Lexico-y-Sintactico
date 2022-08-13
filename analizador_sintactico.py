from regla_semantica import *
from lark import Lark, Transformer

class Analizador_Sintactico:
    def __init__(self, text):
        self.text=text
    
    def compilar(self):
        parser= Lark()