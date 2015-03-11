man = []
other = []
try:
	data = open('sketch.txt')

	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			"""strip() is clean space in string"""
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other man':
				other.append(line_spoken)
		except ValueError:
			pass

	data.close()
except IOError:
	print('The data file is missing!!!!')
try:
	with open('man.txt','w')as man_file:
		print(man , file =man_file)
	with open('other.txt','w')as other_file:
		print(other , file = other_file)
except IOError as err:
	print('File error:'+ str(err))
