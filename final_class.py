import time_string
class AtheteList(list):
	def __init__(self,a_name,a_dob=None,a_times =[]):
		list.__init__([])
		self.name = a_name
		self.dob  = a_dob
		self.extend(a_times)
	def top3(self):
		return(sorted(set([time_string.santize(t) for t in self]))[0:3])

vera = AtheteList('vera vi')
vera.append('1.35')
print(vera.name)
print(vera.top3())
vera.extend(['1.55','1.02','1.30'])
print(vera.top3())