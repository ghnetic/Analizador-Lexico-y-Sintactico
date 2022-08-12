#Importacion de expresiones regulares
import re

class AnalizadorLexico:
    def __init__(self, reader, name):
        self.reader=reader
        self.archivo=name
        self.texto=self.reader.texto
        self.tokens={}
    
    def contadorLineas(self):
        linea=0
        texto=re.split(r"\n", self.texto)
        for numLinea in texto:
            print("Probando contador...")
            print(re.split(r"\s", numLinea.replace("\'",'')))
            linea+=1
            self.tokens[linea]=re.split(r"\s", numLinea)
        print(self.tokens)
        print(linea)
        return self

    
