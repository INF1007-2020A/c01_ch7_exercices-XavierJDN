#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import turtle
import time
from ch6 import histogram

# TODO: Définissez vos fonction ici
def ellipse(M: int, a: int = 1, b: int = 2, c: int = 3) -> tuple:
    v = (4 / 3) * pi * a * b * c
    m = v / M
    return v, m

def sort(histogram: dict, sequence: str = "feefgg") -> tuple:
    dict_squence ={}
    list_letter = sorted(histogram(sequence).items(), reverse=True, key = lambda x: x[1])
    for i in range(len(list_letter)):
        dict_squence[list_letter[i][0]] = list_letter[i][1]
    return list_letter[0][0], dict_squence[list_letter[0][0]]
def trees(length_branch: int):

    if length_branch <= 10:
        return
    else:
        turtle.forward(length_branch)
        turtle.left(30)
        trees(3*length_branch/4)
        turtle.right(60)
        trees(3*length_branch/4)
        turtle.left(30)
        turtle.backward(length_branch)
    #reference: https://i.ytimg.com/vi/6dcp_gxnv-Q/maxresdefault.jpg

def is_adn(s: str) -> bool:
    
    if s == "":
        return False
    for char in s:
        if not(char == "a" or char == "t" or char == "g" or char == "c"):
            return False
    return True

def adn_str(valid_adn: bool) -> str:
    s = ""
    while True:
        char = input("Ecrire un charactere valide: ")
        while valid_adn(char) == False:
            char = input("Ecrire un charactere valide: ")
        s += char
        finish = input("Avez vous finit(y/n): ")
        if finish == "y": 
            return s

def proportion(chaine: str,sequence: str = "ca") -> tuple:
    occurence = 0
    for reference in range(0, len(chaine)):
        if chaine[reference:reference + len(sequence) ] == sequence:
            print(reference)
            occurence += 1
    print(occurence)
    prop = occurence  / len(chaine)
    return prop,sequence
        
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # for i in range(0,10):
    #     volume, masse = ellipse(i,i+1,i+2,36)
    #     print(f"le volume est {volume}et sa masse est {masse}")
    # turtle.speed(0)
    # turtle.left(90)
    # trees(100)
    # time.sleep(10)
    # adn = input("Donez un adn: ")
    # match_sequence, sequence = proportion(adn)
    # # print(f" la chaine de charatere est : {is_adn(adn)} un adn ")
    # print(f"Il y a {round(match_sequence * 100, 2)} % de {sequence}")
    # # print(adn_str(is_adn))
    
    sequence = "argrgthy"
    print(sort(histogram))