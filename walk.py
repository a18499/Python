import os
import subprocess


file_list = []
flag =0
count_ckeck =0
#file_out = subprocess.check_output(['ls /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/virus/'],shell=True)
file_out = subprocess.check_output(['ls /home/peter/test_virus/'],shell=True)
file_list = str(file_out).strip("b '").strip("'").split("\\n")
for each_word in file_list:
	print(each_word,end ="\n")
	os.system("unzip "+"/home/peter/test_virus/"+each_word+" -d /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/"+each_word+"/")
	for root, dirs, files in os.walk("/media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/"+each_word):
    		print (root)
    		print (dirs)
    		print (files)
    		for each_file in files:
    			if each_file == "libsecexe.x86.so":
    				print("find it!!!!!!!!!!!!!!!!!!!!!!!!Bangcle",end ="\n")
    				flag =1
    			elif  each_file == "libsecexe.so":
    				print("find it!!!!!!!!!!!!!!!!!!!!!!!!Bangcle",end ="\n")
    				flag =1
    			elif each_file == "libspkprotect2.so":
    				print("find it!!!!!!!!!!!!!!!!!!!!!!!!ApkProtect",end ="\n")
    				flag =1
    			elif each_file ==  "libexecmain.so ":
    				print("find it!!!!!!!!!!!!!!!!!!!!!!!!ApkProtect",end ="\n")
    				flag =1
	if flag == 1:
    		flag =0
    		count_ckeck=count_ckeck +1
    		print("Check"+str(count_ckeck)+" file")
	else:
		count_ckeck=count_ckeck +1
		print("Check"+str(count_ckeck)+" file")
		os.system("rm -r -f  /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/"+each_word)