from tkinter import *
import tkinter.font as tkFont
import os.path
import keyboard
import webbrowser


versionNo = "v0.3"



def initializeTextFiles():
    file = open("DeathCounter.txt", "w+")
    file.write("0")
    file.close()

def callback(url):
    webbrowser.open_new(url)

class Deaths():
    def __init__(self,Deaths,DeathLimit):
        self.deaths = Deaths #deaths
        self.limit = DeathLimit #default death count
    # function to add a death
    def addDeath(self):
        self.deaths += 1
        deathsCountLabel.config(text=str(self.deaths))
        print("Death count is now:",self.deaths)
    # function to remove a death
    def removeDeath(self):
        if self.deaths > 0:
            self.deaths -= 1
            deathsCountLabel.config(text=str(self.deaths))
            print("New death count:", self.deaths)
        else:
            print("Already at 0")
    def resetDeaths(self):
        self.deaths = 0
        deathsCountLabel.config(text=str(self.deaths))
        print("Deaths set to:",self.deaths)

gameRules = Deaths(0,10)


#hotkeys

hotkeyUp = "Ctrl+Shift+D"
hotkeyDown = "Ctrl+Shift+G"
hotkeyReset = "Ctrl+Shift+0"

keyboard.add_hotkey(hotkeyUp,gameRules.addDeath)
keyboard.add_hotkey(hotkeyDown,gameRules.removeDeath)
keyboard.add_hotkey(hotkeyReset,gameRules.resetDeaths)



# Build UI
# Create Main Window
main = Tk()
main.title("Big Secret's Deaths Counter")
main.configure(bg="gray7")
main.resizable(False,False)
main.minsize(200,50)
mainIconAbs = os.path.abspath("Icon.png")
mainIcon = PhotoImage(file=mainIconAbs)
main.iconphoto(False,mainIcon)

# Create pieces.
fontStyle = tkFont.Font(family="System", size=12)
headerFont = tkFont.Font(family="System", size=30)
versionLabel = Label(main,text=(str(versionNo+", © BigSecret")),bg='gray7',fg='dodger blue')
deathsLabel = Label(main,text="Deaths:", bg='gray7',fg='white')
deathsCountLabel = Label(main, text="0", bg='gray7', fg='white', font=headerFont,width=3)
addDeathButton = Button(main, text="+", bg='orangered', fg='white', font=fontStyle,command=gameRules.addDeath)
removeDeathButton = Button(main, text="-", bg='gray20', fg='white',font=fontStyle, command=gameRules.removeDeath)
resetDeathButton = Button(main,text="Reset",bg="gray20",fg="white",font=fontStyle, command=gameRules.resetDeaths)
hotkeyLabel = Label(main,text="--Hotkey--",bg='gray20',fg='white')
addDeathHotkeyLabel = Label(main,text=str(hotkeyUp),bg='gray20',fg='white')
removeDeathHotkeyLabel = Label(main,text=str(hotkeyDown),bg='gray20',fg='white')
resetHotkeyLabel = Label(main,text=str(hotkeyReset),bg='gray20',fg='white')

# Place Pieces.
#deathsLabel.grid(row=0,column=1, sticky="SNEW", pady=15, padx=15)
versionLabel.place(x=5,y=120,anchor="w")
versionLabel.bind("<Button-1>", lambda e: callback("https://www.bigsecret.live"))
deathsCountLabel.grid(row=0,column=1, rowspan=3, sticky="SNEW", pady=(30,15), padx=(40,15))
addDeathButton.grid(row=1,column=2,sticky="SNEW",pady=(15,5), padx=(40,15))
removeDeathButton.grid(row=2,column=2,sticky="SNEW",pady=5, padx=(40,15))
resetDeathButton.grid(row=3,column=2,pady=5, padx=(40,15))
#hotkeyLabel.grid(row=0,column=3,sticky="SNEW")
addDeathHotkeyLabel.grid(row=1,column=3,sticky="EW")
removeDeathHotkeyLabel.grid(row=2,column=3,sticky="EW")
resetHotkeyLabel.grid(row=3,column=3,sticky="EW")
# Run app
if __name__ == '__main__':
    initializeTextFiles()
    main.mainloop()
