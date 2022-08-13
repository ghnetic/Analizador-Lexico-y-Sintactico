# Importacion de expresiones regulares
import re


class Analizador_Lexico:
    def __init__(self, reader, name):
        self.reader = reader
        self.archivo = name
        self.patterns = []
        self.text = self.reader.text
        self.tokens = {}
        self.t = ""
        self.contador = 0

    def contadorLineas(self):
        linea = 0
        text = re.split(r"\n", self.text)
        for numLinea in text:
            print(re.split(r"\s", numLinea.replace("\'", '')))
            linea += 1
            self.tokens[linea] = re.split(r"\s", numLinea)
        print(self.tokens)
        print(linea)
        return self

    def tabla(self):
        patterns = []

        for key in self.tokens:
            for token in self.tokens[key]:
                if(token != ''):

                    if self.contador > 0:
                        if re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", token):
                            if re.match(r"^[a-zA-Z][a-zA-Z0-9_]*\'$", token):

                                self.t = self.t + " " + \
                                    token.replace("'", '')
                                self.contador = 0

                                patterns.append(
                                    [key, self.t, "Cadena Identificada"])
                                self.t = ""
                            self.t = self.t + " " + token
                            self.contador = 0

                    elif re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", token):
                        patterns.append(
                            [key, token, "Identificador"])

                    elif re.match(r"^\'[^\']*\'$", token):
                        patterns.append(
                            [key, token, "Cadena Identificada"])

                    elif re.match(r"^=$", token):
                        patterns.append(
                            [key, token, "Operador de asignacion"])

                    elif re.match(r"^\$$", token):
                        patterns.append(
                            [key, token, "Fin de linea identificado"])

                    elif re.match(r"^\d+(\.\d+)?$", token):
                        patterns.append(
                            [key, token, "Numero identificado"])

                    elif re.match(r"^\+*$", token):
                        patterns.append([key, token, "Operador de Suma"])

                    elif re.match(r"^\-*$", token):
                        patterns.append([key, token, "Operador de Resta"])

                    elif re.match(r"^\**$", token):
                        patterns.append([key, token, "Operador de Repeticion"])

                    elif re.match(r"^\.$", token):
                        patterns.append(
                            [key, token, "Operador de concatenacion"])

                    elif re.match(r"^imprimirResultado\([a-z0-9+*\-'.]*\)$", token):
                        patterns.append(
                            [key, token, "Funcion de impresion"])

                    elif re.match(r"^\'[a-zA-Z][a-zA-Z0-9_]*$", token):
                        print("entro1")
                        self.t = self.t + token.replace("'", '')
                        self.contador = 1

                    elif re.match(r"^[a-zA-Z][a-zA-Z0-9_]*\'$", token):
                        print("entro3")
                        self.t = self.t + " " + token.replace("'", '')
                        print(self.t)
                        self.contador = 0

                        patterns.append(
                            [key, self.t, "Cadena Identificada"])
                        self.t = ""

                    else:
                        quit(
                            "Error: \n\ttoken desconocido en la linea %s: %s \n\n" % (
                                self.buscarLineaErrorToken(token),
                                token
                            )
                        )

        self.patterns = patterns
        return self

    def buscarLineaErrorToken(self, token):
        lineaError = 0

        f = open(self.archivo, 'r')
        for linea in f:
            lineaError += 1
            if re.match(r'^.*%s.*$' % self.prevenir(token), linea):

                break
        f.close()
        return lineaError

    def prevenir(self, token):

        if re.match(r'[\+\*\.\(\)\{\}\[\]\\\<\>]', token):
            return '\\%s' % token
