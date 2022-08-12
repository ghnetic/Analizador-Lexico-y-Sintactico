from AnalizadorSintactico import *
from AnalizadorLexico import *
from tabulate import tabulate
import sys

class Reader():
    def __init__(self): 
        self.instruction = None
        self.fileName = None
        self.text = None

    def read(self):
        self.params = sys.argv[1:]

        try:
            if len(self.params) == 1:
                self.fileName =  self.params[0]
                f = open(self.fileName,'r')
                self.text = f.read()
                f.close()

            else:
                quit("Error: cantidad de parametros no son validos")
        except FileNotFoundError as e:
            quit("Error %s"%e)
        return self 

reader = Reader().read()
name = Reader().read().fileName

if reader.instruction == None:
    print("\n-----------------------        Analisis Lexico         -----------------------\n")
    tokens = AnalizadorLexico(reader, name ).convertirArchivo().tablaAnalizadorLexico().patrones
    encabezadoTabla = ['# Linea','Token','Descripcion']
    if len(tokens) > 0:
        print(tabulate(tokens, encabezadoTabla, tablefmt="grid"))
    else:
        print("----------------------------------------------------")
    print("\n-----------------------        Analisis Sintactico         -----------------------\n")
    AnalizadorSintactico(reader.text).run()
else:
    quit("No se esta especificando la  instrucción ")




