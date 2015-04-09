from tkinter import *

from tkinter import *
import sys
import time
import os
import hashlib
class GUIDemo(Frame):
    global hide 
    global superuser
    global browser 
    global contact 
    hide = 0
    superuser = 0
    browser = 0
    contact = 0
    def Browser(self,Parammeter):
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

    def show_result(self):
        if hide != 0:
             self.displayText2["text"] = "Hide File [V]"
        else:
            self.displayText2["text"] = "Hide File [ ]"
        if superuser != 0:
            self.displayText3["text"] = "Super User [V]"
        else:
            self.displayText3["text"] = "Super User [ ]"
        if browser != 0:
            self.displayText4["text"] = "Browser History [V]"
        else:
             self.displayText4["text"] = "Browser History [ ]"
        if contact !=0 :
            self.displayText5["text"] = "Contact [V]"
        else:
            self.displayText5["text"] = "Contact [ ]"

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "APK:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=6)

        self.inputText2 = Label(self)
        self.inputText2["text"] = "RULE:"
        self.inputText2.grid(row=1, column=0)
        self.inputField2 = Entry(self)
        self.inputField2["width"] = 50
        self.inputField2.grid(row=1, column=1, columnspan=6)

        self.inputText3 = Label(self)
        self.inputText3["text"] = "Duration:"
        self.inputText3.grid(row=2, column=0)
        self.inputField3 = Entry(self)
        self.inputField3["width"] = 50
        self.inputField3.grid(row=2, column=1, columnspan=6)
        self.start = Button(self)
        self.start["text"] = "Start"
        self.start.grid(row=3, column=0,columnspan=6)
        self.start["command"] =  self.startMethod
        self.load = Button(self)
        self.load["text"] = "Load"
        self.load.grid(row=1, column=7)
        self.load["command"] =  self.loadMethod
        self.load2 = Button(self)
        self.load2["text"] = "Load"
        self.load2.grid(row=0, column=7)
        self.load2["command"] =  self.load2Method

        self.displayText = Label(self)
        self.displayText["text"] = "Dynamic APP Behavior Monitor"
        self.displayText.grid(row=4, column=0, columnspan=7)

        self.displayText2 = Label(self)
        self.displayText2["text"] = "Result"
        self.displayText2.grid(row=5, column=0, columnspan=7)

        self.displayText2 = Label(self)
        self.displayText2["text"] = "Result"
        self.displayText2.grid(row=5, column=0, columnspan=7)

        self.displayText3 = Label(self)
        self.displayText3.grid(row=6, column=0, columnspan=7)

        self.displayText4 = Label(self)
        self.displayText4.grid(row=7, column=0, columnspan=7)

        self.displayText5 = Label(self)
        self.displayText5.grid(row=8, column=0, columnspan=7)

        self.displayText6 = Label(self)
        self.displayText6.grid(row=9, column=0, columnspan=7)

    def loadMethod(self):
        self.displayText["text"] = self.inputField.get()

    def load2Method(self):
        self.displayText["text"] = "This is Load2 button"
   
    def startMethod(self): 
        
        os.system("/home/peter/Android/Sdk/platform-tools/adb install "+self.inputField.get())
        os.system("/home/peter/Android/Sdk/platform-tools/adb logcat -c")
        os.system("/home/peter/Android/Sdk/platform-tools/adb shell am start -n com.example.peter.test/.MainActivity")
        (path,apk_name)= os.path.split(self.inputField.get())
        apk_size = os.path.getsize(self.inputField.get())
        duartion = int(self.inputField3.get())
        apk_file = open(self.inputField.get(),'rb')
        sha256_check = hashlib.sha256()
        sha256_check.update(apk_file.read())
        for x in range(duartion):
            print(x)
            time.sleep(1)
        
        os.system("/home/peter/Android/Sdk/platform-tools/adb logcat -v threadtime -s -d DroidBox:V > /home/peter/Analize-log/anaylize-log.txt ")
        try:
             the_file = open("/home/peter/Analize-log/anaylize-log.txt")
             the_file.seek(0) 
             for each_line in the_file: 
                 self.Browser(each_line)
             the_file.close()
        except IOError:
            print("Cannot open file")
        finally:
            self.displayText["text"] = "----------------------------Anaylize Result--------------------"+"\n"+"-----------APK Information----------------------------------"+"\n"+"APK name: "+apk_name+"\n"+"APK size: "+str(apk_size)+" byte"+"\n"+"SHA256: "+sha256_check.hexdigest()+"\n"+"-----------APK Behavior----------------------------------------"
           # self.displayText["text"].append = "----------------------------Anaylize Result--------------------"+"\n"
            print("----------------------------Anaylize Result--------------------",end='\n')
            print("-----------APK Information----------------------------------",end='\n')
            print("APK name: "+apk_name,end='\n')
            print("APK size: "+str(apk_size)+" byte",end='\n')
            print("SHA256: "+sha256_check.hexdigest())
            print("-----------APK Behavior----------------------------------------",end='\n')
            self.show_result()

            print("==========================================",end='\n')    
    
if __name__ == '__main__':
    root = Tk()
    app = GUIDemo(master=root)
    app.mainloop()