from analizador_lexico import *
from analizador_sintactico import *
from tabulate import tabulate
import sys


class Reader():
    def __init__(self):
        self.instruction = None
        self.fileName = None
        self.text = None

    def read(self):
        # Para leer el archivo .txt
        self.params = sys.argv[1:]

        try:
            if len(self.params) == 1:
                self.fileName = self.params[0]
                f = open(self.fileName, 'r')
                self.text = f.read()
                f.close()

            else:
                quit("Error: cantidad de parametros no son validos")
        except FileNotFoundError as e:
            quit("Error %s" % e)
        return self


reader = Reader().read()
name = Reader().read().fileName

if reader.instruction == None:
    print("\n* * * * * * * * * * A N A L I Z A D O R   L E X I C O * * * * * * * * *\n")
    tokens = Analizador_Lexico(
        reader, name).contadorLineas().tabla().patterns
    print("Cantidad de tokens: ", len(tokens))
    encabezadoTabla = ['Numero de Linea', 'Token', 'Tipo de Token']
    if len(tokens) > 0:
        print(tabulate(tokens, encabezadoTabla, tablefmt="fancy_grid"))
    else:
        print("* * * * * No se pudo :( * * * * *")
    print("\n* * * * * * * * * * A N A L I Z A D O R   S I N T A C T I C O * * * * * * * * * *\n")
    Analizador_Sintactico(reader.text).compilar()
else:
    quit("Error")
