# -*- coding: utf-8 -*-

grammar = """
    //Axioma inicial
    ?start: exp+

    //Definición de una expresión
    ?exp: variable "=" cadena "$" -> asignacion
        | variable "=" operacion "$" -> asignacion
        | variable "=" numero "$" -> asignacion
        | variable "=" repeticion "$" -> asignacion
        | variable "=" concatenacion "$" -> asignacion
        | "imprimirResultado" "("? cadena ")"? "$" -> imprimircadena
        | "imprimirResultado" "("? variable ")"? "$" -> imprimirvariable
        | "imprimirResultado" "("? operacion ")"? "$" -> imprimirop
        | "imprimirResultado" "("? repeticion ")"? "$" ->imprimir
        | "imprimirResultado" "("? concatenacion ")"? "$" ->imprimir

    //Definicion de funcion repeticion
    ?repeticion: numero "*" cadena -> repetir

    //Definicion de funcion concatenacion
    ?concatenacion: parametroconcat "." parametroconcat -> concatenar
        | parametroconcat "." concatenacion -> concatenardos
    
    //Definición de operacion
    ?operacion: elemento
        | operacion "+" elemento -> sumar
        | operacion "-" elemento -> restar

    //Definicion de elemento
    ?elemento: numero
        | variable -> obtenervariable
        | "-"elemento
        | "(" operacion ")"

    //Definicion de parametroconcat
    ?parametroconcat: numero
        | variable
        | cadena

    //Definicion de cadena
    ?cadena: /'[^']*'/
        | /"[^"]*"/

    //Definicion de numero
    ?numero: /\d+(\.\d+)?/

    //Definicion de variable
    ?variable: /[a-zA-Z]\w*/

    //Ignora espacios en blanco y saltos de linea
    %ignore /\s+/
"""
