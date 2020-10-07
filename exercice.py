#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import turtle

# TODO: Définissez vos fonction ici
def ellipse(a:int=1, b:int =2, c: int=3, M:int ) -> tuple:
    v = (4 / 3) * pi * a * b * c
    m = v / M
    return v, m

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    for i in range(0,10):
        volume, masse = ellipse(i,i+1,i+2,36)
        print(f"le volume est {volume}et sa masse est {masse}")

