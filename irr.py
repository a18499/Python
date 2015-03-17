import time_string
with open('julie.txt') as jdata:
	"""Read a line to list """
	data = jdata.readline()
Julies = data.strip().split(',')
print(Julies)
with open('james.txt') as jdata:
	"""Read a line to list """
	data = jdata.readline()
James = data.strip().split(',')
print(James)
with open('sarah.txt') as jdata:
	"""Read a line to list """
	data = jdata.readline()
Sarah = data.strip().split(',')
print(Sarah)
with open('mikey.txt') as jdata:
	"""Read a line to list """
	data = jdata.readline()
Mikey = data.strip().split(',')
print(Mikey)
"""Sorting"""


print("Sorting result")
print(sorted([time_string.santize(each_t) for each_t in James]))
print(sorted([time_string.santize(each_t) for each_t in Julies]))
print(sorted([time_string.santize(each_t) for each_t in Mikey]))
print(sorted([time_string.santize(each_t) for each_t in Sarah]))