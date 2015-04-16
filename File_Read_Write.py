the_file = open('OB_log.txt')
print(the_file.readline(),end='\n')
test_list = []
print("Read Mutiple Line",end='\n')
""" Back to the first line!!! """
the_file.seek(0) 
for each_line in the_file: 
	test_list = each_line.split("\\n")
	
print("===========================",end='\n')
print(test_list)
the_file.close()
