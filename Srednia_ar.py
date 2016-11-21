
# coding: utf-8

# In[2]:

def srednia(lista):
    """Oblicza srednia arytmetyczna ciagu liczb podanych jako lista"""
    if sprawdz(lista)==True:
        x=0
        for k in lista:
            x+=k
        return("RESULT: "+str(x/len(lista)))
    else:
        return("FAILED: WRONG TYPES")

def sprawdz(lista):
    ret=False
    if type(lista)==list or type(lista)==tuple:
        for k in lista:
            if type(k)==int or type(k)==float:
                ret=True
            else:
                return False
        return ret
    else:
        return False

print(srednia([1,2,"a",3]))
print(srednia([1,2,3,4]))