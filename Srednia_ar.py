
# coding: utf-8

# In[2]:

def srednia(lista):
    """Oblicza srednia arytmetyczna ciagu liczb podanych jako lista"""
    x=0
    for k in lista:
        x+=k
    return(x/len(lista))

