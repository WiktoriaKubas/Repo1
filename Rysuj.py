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
		for check in self.dic:
			if self.dic[check] > 70:
				return self.rysujduzyhisto()
		return self.rysujmalehisto()
	
	def rysujmalehisto(self):

		ldic = []
		histogram = []
        	for i in self.dic:
			
			ldic.append(i)

		ldic.sort()
		
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
			print str(histogram[x]) + " : " + str(histogram[x+1])					
		return histogram	
	
	def rysujduzyhisto(self):
                ldic = []
                histogram = []
                for i in self.dic:

                        ldic.append(i)
                ldic.sort()

                for j in ldic:
                        counter = self.dic[j]
                        n = 0
                        temp = ""
                        while n < counter:
                                temp += "="                     
				if "==========" in temp:		
					temp = temp.replace("==========", "#")
				if "##########" in temp:
					temp = temp.replace("##########", "*")
				if "**********" in temp:
					temp = temp.replace("**********", "$")
				n += 1	
                        histogram.append(j)
			histogram.append(temp)
				
		for x in range(0, len(histogram), 2 ):
			print str(histogram[x]) + " : " + histogram[x+1]					

                return histogram   
