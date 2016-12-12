class PROG():

    def __init__(self):
        pass

    def funkcja(self,name):
        source=open(name+".txt").read()
        source=source.replace(",","")
        source=source.replace(".","")
        source=source.replace(";","")
        source=source.replace(":","")
        source=source.replace("\n"," ")
        IN=source.split(" ")
        dic={}
        for i in IN:
            if len(i) in dic:
                dic[len(i)]=dic[len(i)]+1
            else:
                dic[len(i)]=1
        while True:
            ask=input("Wyswietlic wyniki(1) czy zapisac do pliku(2)?")
            if ask=="1":
                return dic
            elif ask=="2":
                target=input("Podaj nazwe pliku(bez rozszerzenia): ")
                temp=dic.items()
                string=""
                for i in temp:
                    string+=(str(i[0])+": "+str(i[1])+"\n")
                out=open(target+".txt",'w')
                out.write(string)
                out.close()
                return(target+".txt")
            else:
                print("Nieprawidlowa komenda!")
                    
P=PROG()
P.funkcja("Dlugosci")
