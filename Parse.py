def Browser(Parammeter):
	if 'browser' in Parammeter:
		print("found browser")
	if 'contacts' in Parammeter:
		print("found contact!")




the_file = open('provider-log')
print(the_file.readline(),end='\n')
print(the_file.readline(),end='\n')
print("Read Mutiple Line",end='\n')
""" Back to the first line!!! """
the_file.seek(0) 
for each_line in the_file: 
	Browser(each_line)
	#print(each_line,end='\n')
print("===========================",end='\n')
the_file.close()
