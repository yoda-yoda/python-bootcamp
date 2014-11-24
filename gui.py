#simple GUI

from Tkinter import *

#create window
root = Tk()

#modify root window
root.title("Deebeat City")
root.geometry("460x600")

#create frames and hold other widgets eg label,button
app = Frame(root)
message = "Client server communication"
app.grid()
label = Label(app, text =message.upper())
label.grid()

clientBtn = Button(app, text="Client")
clientBtn.grid()

serverBtn = Button(app, text="Server")
serverBtn.grid()

#kick off the event loop
root.mainloop()