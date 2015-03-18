import time_string

def get_cocah_data(filename):
	try:
		with open(filename) as jdata:
			"""Read a line to list """
			data = jdata.readline()
		return (data.strip().split(','))
	except IOError:
		return(None)
sarah = get_cocah_data('sarah2.txt')
(sarah_name ,sarah_job) = sarah.pop(0), sarah.pop(0)
print(sarah_name+"'s fastest times are: "+str(sorted(set([time_string.santize(t) for t in sarah]))[0:3]))
