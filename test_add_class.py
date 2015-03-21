import time_string
class Athlete:
	def __init__(self,a_name,a_dob=None,a_times =[]):
		self.name = a_name
		self.dob  = a_dob
		self.times = a_times

	def top3(self):
		return(sorted(set([time_string.santize(t) for t in self.times]))[0:3])
	def add_time(self,time_value):
		self.times.append(time_value)
	def add_times(self,time_list):
		self.times.extend(time_list)

vera = Athlete('vera vi')
vera.add_time('1.35')
print(vera.name)
print(vera.top3())
vera.add_times(['1.55','1.02','1.30'])
print(vera.top3())