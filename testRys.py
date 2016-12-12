from Rysuj import Rysuj

P=Rysuj({3 : 5, 5: 3, 1: 1, 2 : 3})
P2=Rysuj({10 : 100, 71: 200, 30: 30})
#print P.rysujhisto()
temp = ""
n = 20
while n < 21:
	temp += "="
	temp.replace("==========", "#")
	n+=1
print temp
print P2.rysujhisto()
