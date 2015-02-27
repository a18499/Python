

"""this is comment!! """

def print_loop(loop_list):
	for loopitem in loop_list:
		if isinstance(loopitem,list):
			print_loop(loopitem)
		else :
		 	print(loopitem)	

#print_loop(movies)
