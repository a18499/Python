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
Julies_S = sorted(Julies)
James_S = sorted(James)
Mikey_S = sorted(Mikey)
Sarah_S = sorted(Sarah)

print("Sorting result")
print(Julies_S)
print(James_S)
print(Sarah_S)
print(Mikey_S)