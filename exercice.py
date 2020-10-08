#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import turtle
import time


# TODO: Définissez vos fonction ici
def ellipse(M: int, a: int = 1, b: int = 2, c: int = 3) -> tuple:
    v = (4 / 3) * pi * a * b * c
    m = v / M
    return v, m


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


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # for i in range(0,10):
    #     volume, masse = ellipse(i,i+1,i+2,36)
    #     print(f"le volume est {volume}et sa masse est {masse}")
    turtle.speed(0)
    turtle.left(90)
    trees(300)
    time.sleep(10)
