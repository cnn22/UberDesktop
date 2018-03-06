import tkinter as tk
#import tkFont
#from PIL import ImageTk, Image

TITLE_FONT = ('Helvetica 50 bold')
BUTTON_FONT = ('Arial 12 bold')
class uberApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        uberDesktop = tk.Frame(self)
        #uberDesktop.geometry('1000x500')

        uberDesktop.configure(background='black')
        uberDesktop.pack()

        #How I handle different frames...
        self.frames = {}
        for page in (uberLoginPage, mainMenuPage):
            frame = page(uberDesktop, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(uberLoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() #raises the frame to the front...aka switch screens


class uberLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        #logo = 'Logobit_digital_black_large.png'
        #uberLogo = ImageTk.PhotoImage(Image.open(logo))
        #panel = Label()
        uberLogo = tk.Label(self, text = 'U B E R', bg='black', fg='white', font=TITLE_FONT)
        uberLogo.pack(pady = 10, padx = 10)

        #emailString = tk.StringVar()
        #emailLogin = tk.Entry(self, textvariable = emailString)
        #emailLogin.pack(pady = 10, padx = 10)
        emailBox = tk.Entry(self)
        #emailBox.insert(0, 'Email')
        #email.Box.bind*"<FocusIn", self.clearWidget())
        emailBox.pack(pady=10, padx=10)

        passwordBox = tk.Entry(self, show='*')
        passwordBox.pack(pady=10, padx=10)

        loginButton = tk.Button(self, text = 'Log In', font = BUTTON_FONT, bg='#808080', fg='white', command=lambda:controller.show_frame(mainMenuPage))
        #loginButton.bind('<return', login)
        loginButton.pack(pady=10, padx=10)

    #def login(self, cont)

class mainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        welcomeLabel = tk.Label(self, text = 'Welcome', fg = 'white', bg='black', font='Helvetica 18 bold')
        displayUsername = tk.Label(self, text = 'Christine Nguyen', fg = '#00e6e6', bg='black', font='Helvetica 18')

        signOutButton = tk.Button(self, text='Sign Out', command=lambda:controller.show_frame(uberLoginPage))
        alterMenuButton = tk.Button(self, text='ALTER') #command=lambda:controller:show_frame(alterMenuPage)

        welcomeLabel.pack( pady=5)
        displayUsername.pack(pady=10)
        signOutButton.pack(fill=tk.X)
        alterMenuButton.pack(fill=tk.X, side='bottom')

    #def signOut(self):
    #def alterMenu
    #def createMenu
    #def lookupMenu


app = uberApp()
app.mainloop()
