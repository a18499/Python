movies = ["The Holy Grailliam","1975","Terry Jones & Terry Gilliam","91",
           ["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]

print(movies)

for each_item in movies:
	if isinstance(each_item,list):
		for each_nest_item in each_item:
			if isinstance(each_nest_item,list):
				for each_inter_nest_item in each_nest_item:
					print(each_inter_nest_item)
			else :
				print(each_nest_item)
	else :
	 	print(each_item)
