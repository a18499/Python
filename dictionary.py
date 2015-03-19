import time_string

def get_cocah_data(filename):
	try:
		with open(filename) as jdata:
			"""Read a line to list """
			data = jdata.readline()
			temp = data.strip().split(',')
		return ({'Name' :temp.pop(0),'DOB' :temp.pop(0),'Times' :str(sorted(set([time_string.santize(t) for t in temp]))[0:3])})
	except IOError:
		return(None)

james = get_cocah_data('james2.txt')
julie = get_cocah_data('julie2.txt')
print(james['Name']+"'s fastest times are: "+james['Times'])
print(julie['Name']+"'s fastest times are: "+julie['Times'])