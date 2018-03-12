import tkinter as tk
from driverTreeview import *
from licenseTreeview import *
from userRatingTreeview import userRating
from addressView import addressRecord
from bankTreeview import bankTreeview
#import mysql.connector
#from mysql.connector import errorcode
#from PIL import ImageTk, Image


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
        for page in (uberLoginPage, mainMenuPage, viewMenu, insertMenu):
            frame = page(uberDesktop, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        #self.startDBConnection("employee")
        self.show_frame(uberLoginPage) #displays the loginPage after firing up the app

    #show_frame is a function that will show the frame that you want to display by "raising it".
    #there is no particular order, it raises whenever you want to raise
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() #raises the frame to the front...aka switch screens

    #create_window creates a child window (another window).
    def create_window(self, name):
        self.counter+=1
        window = tk.Toplevel(self)
        window.wm_title(name)
        window.minsize(height=200, width=1000)
        if name == "Driver's Incident":
            driverIncidentRecord = driverRecord(window) #calling the driverIncidentRecord to make the gui inside the child window
        elif name == "Driver's Bank:":
            driverBankingRecord = bankTreeview(window)
        elif name == "Driver's License":
            driverLicenseRecord = driverLicenseView(window)
        elif name == "User Rating":
            userRatingRecord = userRating(window)
        elif name == "Addresses":
            addresses = addressRecord(window)



    #getTable is a function that will help call create_window and in that window,
    #it will contain the table that was selected for the query
    def getTable(self, selection, controller):
        selection = selection.get()
        print(selection)
        if selection == "Driver's Incident":
            controller.create_window("Driver's Incident")
        elif selection == "Driver's Bank":
            controller.create_window("Driver's Bank")
        elif selection == "Driver's License":
            controller.create_window("Driver's License")
        elif selection == "Address":
            controller.create_window("Address")
        elif selection == "BankingAccount":
            controller.create_window("BankingAccount")
        elif selection == "User Rating":
            controller.create_window("User Rating")
        elif selection == "Addresses":
            controller.create_window("Addresses")


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

    #def authenticateLogin(self, email, password):

    #def login(self, cont)
    #def clearWidget():

#mainMenuPage is the frame that handles what the main menu will look like
class mainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background='black')

        welcomeLabel = tk.Label(self, text = 'Welcome', fg = 'white', bg='black', font='Helvetica 18 bold')
        displayUsername = tk.Label(self, text = '[user]', fg = '#00e6e6', bg='black', font='Helvetica 18')

        signOutButton = tk.Button(self, text='Sign Out', bg='#008080', fg='white', font = 'Arial 10', command=lambda:controller.show_frame(uberLoginPage)) #this is where the magig happens with the frames!
        viewButton = tk.Button(self, text='VIEW', bg='#008080', fg='white', font = BUTTON_FONT, command=lambda:controller.show_frame(viewMenu)) #command=Lambda:controller.show_frame(createMenuPage)


        insertMenuButton = tk.Button(self, text='INSERT', bg='#008080', fg='white', font = BUTTON_FONT, command=lambda:controller.show_frame(insertMenu))
        lookupMenuButton = tk.Button(self, text='LOOK UP', bg='#008080', fg='white', font = BUTTON_FONT) #command=Lambda:controller.show_frame(lookupMenuPage)

        welcomeLabel.pack( pady=5)
        displayUsername.pack(pady=10)
        signOutButton.config(width=10)
        insertMenuButton.config(width=50)
        #reportButton.config(width=50)
        #reportMenu.pack()
        lookupMenuButton.config(width=50)

        #signOutButton.place(relx=0.0, rely=1.0, anchor='ne')
        signOutButton.pack()
        viewButton.pack(pady=5, ipadx=227, ipady=3)
        insertMenuButton.pack(pady=5, ipady=5)
        lookupMenuButton.pack(pady=5, ipady=5)

    #def alterMenu
    #def createMenu
    #def lookupMenu

#reportMenu is the frame that handles the view selections
class viewMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')

        instructionLabel = tk.Label(self,text="Select which report you would like to perform.", font=GENERAL_FONT,fg='white', bg='black')
        REPORT_OPTIONS = ["Addresses", "Driver's Bank", "Driver's Incident", "Driver's License", "User Rating", "--"]
        selection=tk.StringVar(self)
        selection.set("--")
        viewButton = tk.OptionMenu(self, selection, *REPORT_OPTIONS)
        selectButton = tk.Button(self, text="Select", bg='#008080', fg='white', font = GENERAL_FONT, command=lambda:controller.getTable(selection, controller)) #command=lambd
        backButton = tk.Button(self, text='Back', bg='#008080', fg='white', font = GENERAL_FONT, command=lambda:controller.show_frame(mainMenuPage))

        instructionLabel.pack(pady=10)
        viewButton.pack(padx=210, pady=50)
        selectButton.pack(ipadx=150, ipady = 5, pady=10)
        backButton.pack(ipadx=155, ipady=5)

#insertMenu is a frame that handles what the insert menu should look like
class insertMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')

        instructionLabel = tk.Label(self, text="Choose which table you would like to insert?",
        fg = 'white', bg = 'black', font=GENERAL_FONT)

        INSERT_OPTIONS = ["Address", "BankingAccount", "Driver", "DriverLicense", "Fare", "IncidentRecord", "Receipt", "RideRequest", "RideType", "UberAccount", "UserRating", "Vehicle", "VehicleType", "--"]
        selection=tk.StringVar(self)
        selection.set("--")
        insertButton = tk.OptionMenu(self, selection, *INSERT_OPTIONS)
        selectButton = tk.Button(self, text="Select", bg='#008080', fg='white', font = GENERAL_FONT, command=lambda:controller.getTable(selection, controller)) #command=lambd
        backButton = tk.Button(self, text='Back', bg='#008080', fg='white', font = GENERAL_FONT, command=lambda:controller.show_frame(mainMenuPage))

        instructionLabel.pack(pady=10)
        insertButton.pack(padx=210, pady=50)
        selectButton.pack(ipadx = 150, ipady=5, pady=10)
        backButton.pack(ipadx=155, ipady=5)


app = uberApp()
app.mainloop()
