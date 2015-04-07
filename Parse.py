import sys
import os
global hide 
global superuser
global browser 
global contact 
hide = 0
superuser = 0
browser = 0
contact = 0
def Browser(Parammeter):
	white_list = open(sys.argv[2])
	white_list.seek(0)
	global hide 
	global superuser 
	global browser 
	global contact 
	#print(Parammeter)
	for each_rule in white_list:
		#print(each_rule.strip("\n"))
		(Rule_Tag, Rule) = each_rule.strip("\n").split(":")
		if Rule in Parammeter:
			if Rule_Tag == "Hide File":
				hide = hide +1
			elif Rule_Tag == "Super User":
				superuser = superuser+1
			elif Rule_Tag == "History":
				browser = browser+1
			elif Rule_Tag == "Contact":
				contact = contact+1			
	white_list.close()

def show_result(hide,superuser,browser,contact ):
	if hide != 0:
		print("Hide File [V]")
	else:
		print("Hide File [ ]")
	if superuser != 0:
		print("Super User [V]")
	else:
		print("Super User [ ]")
	if browser != 0:
		print("Browser History [V]")
	else:
		print("Browser History [ ]")
	if contact !=0 :
		print("Contact [V]")
	else:
		print("Contact [ ]")

"""-----------Program Start--------"""		
os.system("/home/peter/Android/Sdk/platform-tools/adb install"+sys.argv[1])
try:
	the_file = open(sys.argv[1])
except IOError:
	print("Cannot open file")
print("Read Mutiple Line",end='\n')
""" Back to the first line!!! """
the_file.seek(0) 
for each_line in the_file: 
	Browser(each_line)
	#print(each_line,end='\n')
show_result(hide,superuser,browser,contact )

print("===========================",end='\n')
the_file.close()
