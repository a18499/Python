import os
import subprocess

log_list = []
try:
	OB = open('OB_log.txt',"w")
except IOError:
	print('File open error!!!')
finally:
	"""Begin to Fetch File List"""
	file_list = []

	#file_out = subprocess.check_output(['ls /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/virus/'],shell=True)
	file_out = subprocess.check_output(['ls /home/peter/test_virus/'],shell=True)
	file_list = str(file_out).strip("b '").strip("'").split("\\n")
	x = 0
	for each_word in file_list:
		#print(each_word,end='\n')
		print("OB file "+str(x))
		out = subprocess.check_output(["java -jar APKdeob.jar -i /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/virus/"+each_word+" -d Nexus_5_API_21_x86 -w /home/peter/APKdeOB_tmp/"], shell=True)
		log_list.append(out)
		print(out,end='\n')
		print("OB file "+str(x)+"complete")
		x=x+1
	print(log_list , file = OB)
	OB.close()
	

"""Begin to Parse log file"""
try:
	OB = open('OB_log.txt')
except IOError:
	print('File open error!!!')