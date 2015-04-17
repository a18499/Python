the_file = open('OB_log.txt')
print(the_file.readline(),end='\n')
test_list = []
print("Read Mutiple Line",end='\n')
""" Back to the first line!!! """
the_file.seek(0) 
for each_line in the_file: 
	test_list = each_line.strip("b '").strip("'").split("\\n")
	
print("===========================",end='\n')
for each_log in test_list:
	print(each_log,end='\n')
the_file.close()