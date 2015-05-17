from ChatFns import *
from twitter import *

WindowTitle = 'Elvirachat v0.1 - Login'
Username=""

#------------------ MOUSE EVENTS -------------------#

def ClickAction():
    #Write message to chat window
    Username = FilteredMessage(EntryBoxUsername.get("0.0",END))
    base.destroy()


#----------------- KEYBOARD EVENTS -----------------#

def PressAction(event):
	EntryBox.config(state=NORMAL)
	ClickAction()


def DisableEntry(event):
	EntryBox.config(state=DISABLED)
    
#-----------------GRAPHICS MANAGEMENT---------------#

#Create a window
base = Tk()
base.title(WindowTitle)
base.geometry("500x300")
base.resizable(width=FALSE, height=FALSE)

#Create the Button to send message
SendButton = Button(base, font=15, text="Login", width="10", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction)

Username = Button(base, font=15, text="Username", width="20", height=5,
                    bd=0, bg="#DFBF00", activebackground="#FACC2E")

#Create the box to enter message
EntryBoxUsername = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBoxUsername.bind("<Return>", DisableEntry)
EntryBoxUsername.bind("<KeyRelease-Return>", PressAction)


EntryBoxUsername.place(x=160, y=110, height=22, width=186)
SendButton.place(x=202, y=180, height=20)
Username.place(x=160, y=130, height=20)


base.mainloop()





