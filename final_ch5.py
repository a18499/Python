import time_string

def get_cocah_data(filename):
	try:
		with open(filename) as jdata:
			"""Read a line to list """
			data = jdata.readline()
		return (data.strip().split(','))
	except IOError:
		return(None)
James = get_cocah_data('james.txt')
print(James)
Julies = get_cocah_data('julie.txt')
print(Julies)
Sarah = get_cocah_data('sarah.txt')
print(Sarah)
Mikey = get_cocah_data('mikey.txt')
print(Mikey)
"""Sorting"""

print("Sorting result")


print(sorted(set([time_string.santize(each_t) for each_t in James]))[0:3]) 
print(sorted(set([time_string.santize(each_t) for each_t in Julies]))[0:3])
print(sorted(set([time_string.santize(each_t) for each_t in Mikey]))[0:3])
print(sorted(set([time_string.santize(each_t) for each_t in Sarah]))[0:3])
