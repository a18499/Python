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

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in James:
	clean_james.append(time_string.santize(each_t))
for each_t in Julies:
	clean_julie.append(time_string.santize(each_t))
for each_t in Sarah:
	clean_sarah.append(time_string.santize(each_t))
for each_t in Mikey:
	clean_mikey.append(time_string.santize(each_t))
print("Sorting result")
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))