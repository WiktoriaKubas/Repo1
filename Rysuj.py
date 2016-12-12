class Rysuj:
	""" klasa rysujaca histogram 
	na wejsciu otrzymuje slownik
	"""
	def __init__(self, dic):
		self.dic = dic
	def rysujhisto(self):
		""" funkcja rysujaca histogram
		"""
		ldic = []
		histogram = []
        	for i in self.dic:
			
			ldic.append(i)

		ldic.sort()
		print ldic
		
		for j in ldic:
			counter = self.dic[j]
			n = 0
			temp = ""
			while n < counter:
				temp += "="
				n += 1
			histogram.append(j)
			histogram.append(temp)
		for x in range(0, len(histogram), 2):
			print str(histogram[x]) + " : " + histogram[x+1]					
		return histogram	

