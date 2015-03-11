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
	manout = open("man.txt","w")
	otherout = open("other.txt","w")

	print(man , file = manout)
	print(other , file = otherout)


except IOError:
	print('File open error!!!')
finally:
	manout.close()
	otherout.close()