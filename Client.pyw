import thread
from ChatFns import *
from twitter import *
from Login import *
import datetime

consumer_key = ""
consumer_secret = ""
access_key = "-"
access_secret = ""


WindowTitle = 'Elvirachat v0.1 - Client'
#---------------------------------------------------#
#------------------ MOUSE EVENTS -------------------#
#---------------------------------------------------#
def ClickAction():
    #Write message to chat window
    EntryText = FilteredMessage(EntryBox.get("0.0",END))
    LoadMyEntry(ChatLog, EntryText)
    #Scroll to the bottom of chat windows
    ChatLog.yview(END)
    #Erace previous message in Entry Box
    EntryBox.delete("0.0",END)      


def BlockAction():
    items = map(int, Userlog.curselection())
    print items   


def twittear():
    EntryText = FilteredMessage(EntryBox.get("0.0",END))
    new_status = EntryText  
    # create twitter API object
    twitter = Twitter(
    auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))
    results = twitter.statuses.update(status = new_status)
    print "updated status: %s" % new_status


#---------------------------------------------------#
#----------------- KEYBOARD EVENTS -----------------#
#---------------------------------------------------#
def PressAction(event):
	EntryBox.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
    EntryBox.config(state=DISABLED)
    

#---------------------------------------------------#
#-----------------GRAPHICS MANAGEMENT---------------#
#---------------------------------------------------#

def Timeupdate(time = datetime.datetime.now().isoformat()):
    Time.insert(END, time )

#Create a window
base = Tk()
base.title(WindowTitle)
base.geometry("600x500")
base.resizable(width=FALSE, height=FALSE)

#Create a Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.insert(END, "Connecting...\n")
ChatLog.config(state=DISABLED)

#Climate 
Climate = Text(base, bd=0, bg="white", height="8", width="10", font="Arial",)
Climate.insert(END, "Sunny...\n")
Climate.config(state=DISABLED)

#Time
Time = Text(base, bd=0, bg="white", height="8", width="10", font="Arial",)
Timeupdate()
Time.config(state=DISABLED)



#Create List for Users
Userlog = Listbox(base, bd=0, bg="white", height="8", width="50", font="Arial", selectmode = EXTENDED)
Userlog.insert(1, "All...","1","2","3","4")


#Bind a scrollbar to the Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

Userscrollbar = Scrollbar(base, command=Userlog.yview, cursor="heart")
Userlog['yscrollcommand'] = Userscrollbar.set

#Create the Button to send message
SendButton = Button(base, font=15, text="Send", width="10", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction)

AddfileButton = Button(base, font=15, text="[+]", width="3", height=5,
                    bd=0, bg="#AFBF00", activebackground="#FACC2E",
                    command=ClickAction)

Tweetbutton = Button(base, font=15, text="Tweet", width="5", height=5,
                    bd=0, bg="#CFBF00", activebackground="#FACC2E",
                    command=twittear)

Blockbutton = Button(base, font=5, text="Block/Unblock", width="10", height=5,
                    bd=0, bg="#FF0000", activebackground="#FF0000",
                    command=BlockAction)



#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)


scrollbar.place(x=376,y=6, height=410)
ChatLog.place(x=6,y=6, height=410, width=370)

Userscrollbar.place(x=582,y=6, height=410)
Userlog.place(x=400,y=6, height=410, width=195)

Climate.place(x=150,y=470, height=20, width=100)
Time.place(x=290,y=470, height=20, width=200)


EntryBox.place(x=102, y=430, height=33, width=403)
SendButton.place(x=6, y=430, height=35)
Blockbutton.place(x=6, y=465, height=25)
AddfileButton.place(x=505, y=430, height=30)
Tweetbutton.place(x=537, y=430, height=30)


#---------------------------------------------------#
#----------------CONNECTION MANAGEMENT--------------#
#---------------------------------------------------#

def ReceiveData():
    try:
        s.connect((HOST, PORT))
        LoadConnectionInfo(ChatLog, '[ Succesfully connected ]\n---------------------------------------------------------------')
    except:
        LoadConnectionInfo(ChatLog, '[ Unable to connect ]')
        return
    
    while 1:
        try:
            data = s.recv(1024)
        except:
            LoadConnectionInfo(ChatLog, '\n [ Your partner has disconnected ] \n')
            break
        if data != '':
            LoadOtherEntry(ChatLog, data)
            if base.focus_get() == None:
                FlashMyWindow(WindowTitle)
                
        else:
            LoadConnectionInfo(ChatLog, '\n [ Your partner has disconnected ] \n')
            break
    #s.close()

thread.start_new_thread(ReceiveData,())


base.mainloop()
    


