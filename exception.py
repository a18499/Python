the_file = open('sketch.txt')

for each_line in the_file: 
	try:
		(role,line_spoken) = each_line.split(':', 1)
		print(role ,end=' ')
		print("said:",end=' ')
		print(line_spoken,end='')
	except:
		pass
	
print("===========================",end='\n')
the_file.close()