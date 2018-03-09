import tkinter as tk
from driverTreeview import*

TITLE_FONT = ('Helvetica 50 bold')
BUTTON_FONT = ('Arial 12 bold')
GENERAL_FONT =('Helvetica 12 bold')

#uberApp is the class that handles the initalization and frames of the entire application.
#PLEASE USE THIS WHEN TESTING AND BUILDING FRAMES!!!
class uberApp(tk.Tk):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        uberDesktop = tk.Frame(self)
        self.geometry('1000x500')
        self.configure(background='black')
        uberDesktop.configure(background='black')
        uberDesktop.pack(pady=100, padx=100)

        #the frames are handled here. I put all my frames here...
        self.frames = {}
        for page in (uberLoginPage, mainMenuPage, reportMenu):
            frame = page(uberDesktop, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(uberLoginPage) #displays the loginPage after firing up the app

    #show_frame is a function that will show the frame that you want to display by "raising it".
    #there is no particular order, it raises whenever you want to raise
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() #raises the frame to the front...aka switch screens

    def create_window(self, name, controller):
        self.counter+=1
        window = tk.Toplevel(self)
        window.title(name)
        window.minsize(height=200, width=1000)
        driverIncidentRecord = driverRecord(window)
        myDB = tk.Frame(driverIncidentRecord)
        self.show_frame(myDB)


#uberLoginPage is the frame that handles what the login page will look like
class uberLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background='black')
        uberLogo = tk.Label(self, text = 'U B E R', bg='black', fg='white', font=TITLE_FONT)
        uberLogo.pack(pady = 10, padx = 10)

        emailBox = tk.Entry(self)
        #emailBox.insert(0, 'Email')
        #email.Box.bind*"<FocusIn", self.clearWidget())
        emailBox.config(width=50)
        emailBox.pack(pady=10, padx=10)

        passwordBox = tk.Entry(self, show='*')
        passwordBox.config(width=50)
        passwordBox.pack(pady=10, padx=10)

        loginButton = tk.Button(self, text = 'Log In', font = BUTTON_FONT, bg='#333333', fg='white', command=lambda:controller.show_frame(mainMenuPage)) #this is where the magic happens with the frames
        #loginButton.bind('<return', login)
        loginButton.config(width=30)
        loginButton.pack(pady=10, padx=10, ipady=5)
    #def login(self, cont)
    #def clearWidget():
#mainMenuPage is the frame that handles what the main menu will look like
class mainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background='black')


        #selection = tk.StringVar(self)
        #selection.set(REPORT_OPTIONS[0])
        #reportMenu = tk.OptionMenu(self, selection, *REPORT_OPTIONS)

        welcomeLabel = tk.Label(self, text = 'Welcome', fg = 'white', bg='black', font='Helvetica 18 bold')
        displayUsername = tk.Label(self, text = '[user]', fg = '#00e6e6', bg='black', font='Helvetica 18')

        signOutButton = tk.Button(self, text='Sign Out', bg='#008080', fg='white', font = 'Arial 10', command=lambda:controller.show_frame(uberLoginPage)) #this is where the magig happens with the frames!
        reportButton = tk.Button(self, text='REPORTS', bg='#008080', fg='white', font = BUTTON_FONT, command=lambda:controller.show_frame(reportMenu)) #command=Lambda:controller.show_frame(createMenuPage)


        alterMenuButton = tk.Button(self, text='ALTER', bg='#008080', fg='white', font = BUTTON_FONT) #command=lambda:controller.show_frame(alterMenuPage)
        lookupMenuButton = tk.Button(self, text='LOOK UP', bg='#008080', fg='white', font = BUTTON_FONT) #command=Lambda:controller.show_frame(lookupMenuPage)

        welcomeLabel.pack( pady=5)
        displayUsername.pack(pady=10)
        signOutButton.config(width=10)
        alterMenuButton.config(width=50)
        #reportButton.config(width=50)
        #reportMenu.pack()
        lookupMenuButton.config(width=50)

        #signOutButton.place(relx=0.0, rely=1.0, anchor='ne')
        signOutButton.pack()
        reportButton.pack(pady=5, ipadx=210, ipady=5)
        alterMenuButton.pack(pady=5, ipady=5)
        lookupMenuButton.pack(pady=5, ipady=5)

    #def alterMenu
    #def createMenu
    #def lookupMenu
#reportMenu is the frame that handles the report selections
class reportMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')

        instructionLabel = tk.Label(self,text="Select which report you would like to perform.", font=GENERAL_FONT,fg='white', bg='black')
        REPORT_OPTIONS = ["Driver's Incident", "Driver's Bank", "Driver License"]
        selection=tk.StringVar(self)
        selection.set("--")
        reportButton = tk.OptionMenu(self, selection, *REPORT_OPTIONS)
        selectButton = tk.Button(self, text="Select", bg='#008080', fg='white', font = GENERAL_FONT, command=lambda:self.getTable(selection, controller)) #command=lambd

        instructionLabel.pack(pady=10)
        reportButton.pack(padx=210, pady=10)
        selectButton.pack()

    #getQuery is a method that will call create_window from the UberApp class to create a new window,
    #and the correct frame to display the query
    def getTable(self, selection, controller):
        selection = selection.get()
        if selection == "Driver's Incident":
            #controller.show_frame(driverIncident)
            controller.create_window(selection)
        #elif selection == "Driver's Bank":
        #    controller.show_frame
        #elif selection =="Driver License":
        #    controller.show_frame


class alterMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')

app = uberApp()
app.mainloop()
