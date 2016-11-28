class PROG():

    def __init__(self):
        pass

    def funkcja(self,name):
	"""
	:name file
	:return dictionary 
	"""
        source=open(name+".txt").read()
        IN=source.split(" ")
        dic={}
        znaki=[",",".",":","
        for i in IN:
            if(i[-1]=="," or i[-1]=="."):
               i=i[0:(len(i)-1)]
            elif(i[0]=="," or i[0]=="."):
               i=i[1:(len(i))]
            if len(i) in dic:
                dic[len(i)]=dic[len(i)]+1
            else:
                dic[len(i)]=1
        return dic
                    
P=PROG()
