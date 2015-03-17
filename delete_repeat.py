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

uni_james  = []
uni_julies = []
uni_sarah  = []
uni_mikey  = []

print("Sorting result")
print(sorted([time_string.santize(each_t) for each_t in James]))
print(sorted([time_string.santize(each_t) for each_t in Julies]))
print(sorted([time_string.santize(each_t) for each_t in Mikey]))
print(sorted([time_string.santize(each_t) for each_t in Sarah]))

James  = sorted([time_string.santize(each_t) for each_t in James])
Julies = sorted([time_string.santize(each_t) for each_t in Julies])
Mikey = sorted([time_string.santize(each_t) for each_t in Mikey])
Sarah = sorted([time_string.santize(each_t) for each_t in Sarah])

for x in James:
	if x not in uni_james:
		uni_james.append(x)
for x in Julies:
	if x not in uni_julies:
		uni_julies.append(x)
for x in Mikey:
	if x not in uni_mikey:
		uni_mikey.append(x)
for x in Sarah:
	if x not in uni_sarah:
		uni_sarah.append(x)
print("=======TOP 3 ===========")
print(uni_james[0:3])
print(uni_julies[0:3])
print(uni_mikey[0:3])		
print(uni_sarah[0:3])

