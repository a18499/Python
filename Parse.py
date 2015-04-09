import sys
import time
import os
import hashlib
global hide 
global superuser
global browser 
global contact 
hide = 0
superuser = 0
browser = 0
contact = 0
def Browser(Parammeter):
	white_list = open("white_list")
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
switch_index = int(sys.argv[4])

if switch_index == 1:
	os.system("C:/Users/tseyunghuang/AppData/Local/Android/sdk/platform-tools/adb install "+sys.argv[1])
	os.system("C:/Users/tseyunghuang/AppData/Local/Android/sdk/platform-tools/adb logcat -c")
	os.system("C:/Users/tseyunghuang/AppData/Local/Android/sdk/platform-tools/adb shell am start -n com.hideitpro/.AudioDisguiseEntryDefault")
else:
	os.system("/home/peter/Android/Sdk/platform-tools/adb install "+sys.argv[1])
	os.system("/home/peter/Android/Sdk/platform-tools/adb logcat -c")
	os.system("/home/peter/Android/Sdk/platform-tools/adb shell am start -n com.hideitpro/.AudioDisguiseEntryDefault")
(path,apk_name)= os.path.split(sys.argv[1])
apk_size = os.path.getsize(sys.argv[1])

duartion = int(sys.argv[3])
apk_file = open(sys.argv[1],'rb')
sha256_check = hashlib.sha256()

sha256_check.update(apk_file.read())
for x in range(duartion):
	print(x)
	time.sleep(1)
if switch_index == 1:
	os.system("C:/Users/tseyunghuang/AppData/Local/Android/sdk/platform-tools/adb logcat -v threadtime -s -d DroidBox:V > C:/Users/tseyunghuang/Desktop/anaylize-log.txt ")
else:
	os.system("/home/peter/Android/Sdk/platform-tools/adb logcat -v threadtime -s -d DroidBox:V > /home/peter/Analize-log/anaylize-log.txt ")

try:
	if switch_index == 1:
		the_file = open("C:/Users/tseyunghuang/Desktop/anaylize-log.txt")
	else:
		the_file = open("/home/peter/Analize-log/anaylize-log.txt")
	the_file.seek(0) 
	for each_line in the_file: 
		Browser(each_line)
	the_file.close()
except IOError:
	print("Cannot open file")
	
finally:
	print("----------------------------Anaylize Result--------------------",end='\n')
	print("-----------APK Information----------------------------------",end='\n')
	print("APK name: "+apk_name,end='\n')
	print("APK size: "+str(apk_size)+" byte",end='\n')
	print("SHA256: "+sha256_check.hexdigest())
	print("-----------APK Behavior----------------------------------------",end='\n')
	show_result(hide,superuser,browser,contact )

	print("==========================================",end='\n')	
	
