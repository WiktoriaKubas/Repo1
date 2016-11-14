
# coding: utf-8

# In[1]:

#Obliczanie średniej kwadratowej
from math import sqrt
from myerror import *


# In[2]:

def srednia(lista):
    """Oblicznie sredniej kwadratowej"""
    if(type(lista)!=list):
        raise IBeBack
    suma=0.0
    for i in lista:
        suma+=i**2
    return(sqrt(suma/len(lista)))

def srednia2(lista):
    """Obliczanie sredniej arytmetycznej"""
    x=0
    y=len(lista)
    for i in lista:
        x+=i
    return(x/y)