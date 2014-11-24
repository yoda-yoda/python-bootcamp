#simple GUI using oop

from Tkinter import *

class Application(Frame):
	""" GUi app with 3 btns"""

	def __init__(self, master):
		""" Constructor """
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.Btn1 = Button(self, text="Client")
		self.Btn1.grid()

		self.Btn2 = Button(self, text="Server")
		self.Btn2.grid()

		self.Btn3 = Button(self, text="Guest")
		self.Btn3.grid()
		
root = Tk()
root.title("OOP GUI")
root.geometry("460x600")

app = Application(root)

root.mainloop()