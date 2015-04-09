from tkinter import *

from tkinter import *
 
class GUIDemo(Frame):
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
    		self.displayText["text"] = "something happened"
    		self.displayText.grid(row=4, column=0, columnspan=7)
	def loadMethod(self):
    		self.displayText["text"] = self.inputField.get()


	def load2Method(self):
     		self.displayText["text"] = "This is Load2 button"
	def startMethod(self):
     		self.displayText["text"] = "APK Path:"+self.inputField.get()+"RULE Path:"+self.inputField2.get()+"Duration:" +self.inputField3.get()
if __name__ == '__main__':
    root = Tk()
    app = GUIDemo(master=root)
    app.mainloop()