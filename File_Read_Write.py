the_file = open('sketch.txt')
print(the_file.readline(),end='\n')

print("Read Mutiple Line",end='\n')
""" Back to the first line!!! """
the_file.seek(0) 
for each_line in the_file: 
	print(each_line,end='\n')
print("===========================",end='\n')
the_file.close()