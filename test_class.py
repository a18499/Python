import time_string
class Athlete:
	def __init__(self,a_name,a_dob=None,a_times =[]):
		self.name = a_name
		self.dob  = a_dob
		self.times = a_times

	def top3(self):
		return(sorted(set([time_string.santize(t) for t in self.times]))[0:3])


def get_cocah_data(filename):
	try:
		with open(filename) as jdata:
			"""Read a line to list """
			data = jdata.readline()
			temp = data.strip().split(',')
		return Athlete(temp.pop(0),temp.pop(0),temp)
	except IOError:
		return(None)

james = get_cocah_data('james2.txt')
print(james.name + "s fastest times are:"+str(james.top3())) 