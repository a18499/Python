

"""this is the "nester.py" module and it provides one function called print_loop()
   which prints lists that may or may not include nested lists """

def print_loop(loop_list):
        """this function takes one positional argument called "the list", which is any
       python list. Each data item in the provided list is recursively printed to
       the screen on it's own line."""
        for loopitem in loop_list:
                if isinstance(loopitem,list):
                        print_loop(loopitem)
                else:
                        print(loopitem)
		 	
#movies = ["The Holy Grail","The Life of brain","The Meaning of Life"]
#print_loop(movies)
