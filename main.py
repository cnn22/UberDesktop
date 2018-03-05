from tkinter import *

class uberDesktop:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        master.title("Uber Developers")
        master.configure(background = 'white')

        self.uberLogo = Label(frame, text = 'U B E R', bg='black', fg = 'white', font = 'Helvetica 50 bold')
        self.uberLogo.pack()

        self.email = StringVar()
        self.emailLogin = Entry(frame, textvariable = self.email)
        self.emailLogin.pack()

        self.password = StringVar()
        self.passwordLogin = Entry(frame, textvariable = self.password)
        self.passwordLogin.pack()

        self.loginButton = Button(frame, text = 'LOG IN', font = 'Helvetica 15', width = 30, command=self.login)
        #self.loginButton.grid(row = 250, column=250)
        self.loginButton.pack()

        master.geometry("500x200+100+100")

    def login(self):
        print("logged in")

uberWindow = Tk()
my_gui = uberDesktop(uberWindow)
uberWindow.mainloop()
