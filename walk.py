import os
import subprocess


file_list = []
APKProtect_flag =0
Bangcle_flag =0
Ijiami_flag = 0

count_ckeck =0
file_out = subprocess.check_output(['ls /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Virus2/'],shell=True)
#file_out = subprocess.check_output(['ls /home/peter/test_shell_sample/'],shell=True)
file_list = str(file_out).strip("b '").strip("'").split("\\n")
for each_word in file_list:
	print(each_word,end ="\n")
	os.system("unzip "+"/media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Virus2/"+each_word+" -d /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word+"/")
	for root, dirs, files in os.walk("/media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word):
    		try:
    			print (root)
    			print (dirs)
    			print (files)
    			for each_file in files:
    				print(each_file,end ="\n")
    				if each_file == "libsecexe.x86.so":
    					print("find it!!!!!!!!!!!!!!!!!!!!!!!!Bangcle",end ="\n")
    					Bangcle_flag =Bangcle_flag+1
    				elif each_file == "libsecmain.x86.so":
    					Bangcle_flag =Bangcle_flag+1
    				elif  each_file == "libsecexe.so":
    					print("find it!!!!!!!!!!!!!!!!!!!!!!!!Bangcle",end ="\n")
    					Bangcle_flag =Bangcle_flag+1
    				elif each_file == "libsecmain.so":
    					print("find it!!!!!!!!!!!!!!!!!!!!!!!!Bangcle",end ="\n")
    					Bangcle_flag =Bangcle_flag+1
    				elif each_file == "libspkprotect2.so":
    					print("find it!!!!!!!!!!!!!!!!!!!!!!!!ApkProtect",end ="\n")
    					APKProtect_flag =1
    				elif each_file ==  "libexecmain.so ":
    					print("find it!!!!!!!!!!!!!!!!!!!!!!!!",end ="\n")
    					Ijiami_flag =Ijiami_flag+1
    				elif each_word == "libexec.so":
    					Ijiami_flag =Ijiami_flag+1
    		except :
    			print("walk failed")
	print("Bangcle_flag!!!!!!= "+str(Bangcle_flag))
	if APKProtect_flag == 1:
    		APKProtect_flag =0
    		count_ckeck=count_ckeck +1
    		print("in APKProtect_flag!!!!!!!!!!!!!!!!",end ="\n")
    		print("Check"+str(count_ckeck)+" file")
    		os.system("cp -a -r /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word+"/"+" /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Apkprotect/")
    		os.system("rm -r -f  /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word)
	elif Bangcle_flag > 3:
		Bangcle_flag = 0
		count_ckeck=count_ckeck +1
		print("in Bangcle_flag!!!!!!!!!!!!!!!!",end ="\n")
		os.system("cp -a -r /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word+"/"+" /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Bangcle/")
		os.system("rm -r -f  /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word)
		print("Check"+str(count_ckeck)+" file")
	elif Ijiami_flag > 1:
		Ijiami_flag =0
		count_ckeck=count_ckeck +1
		print("in Ijiami_flag!!!!!!!!!!!!!!!!",end ="\n")
		os.system("cp -a -r /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word+"/"+" /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Ijiami/")
		os.system("rm -r -f  /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word)
		print("Check"+str(count_ckeck)+" file")
	else:
		APKProtect_flag =0
		Bangcle_flag = 0
		Ijiami_flag = 0
		count_ckeck=count_ckeck +1
		print("Check"+str(count_ckeck)+" file")
		if each_word != "":
			os.system("rm -r -f  /media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Tmp/"+each_word)