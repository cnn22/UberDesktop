from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from queryBanking import *

class bankTreeview(Frame):

    record = ""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.createUI()
        self.createFilterPanel(parent)
        self.grid(sticky = (N,S,W,E))
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid(row=1, column=0)
        style = Style(self)
        style.configure("Treeview", rowheight=40)

    def createUI(self):
        tv = Treeview(self)
        tv["columns"] = ("Routing#", "Checking#", "Firstname", "Lastname", "4-SSN")
        tv.heading("#0", text="AccountID", anchor="w")
        tv.column("#0", anchor="w", width=75 )
        tv.heading("Routing#", text="Routing#")
        tv.column("Routing#", anchor="center", width=150)
        tv.heading("Checking#", text="Checking#")
        tv.column("Checking#", anchor="center", width=150)
        tv.heading("Firstname", text="Firstname")
        tv.column("Firstname", anchor="center", width=70)
        tv.heading("Lastname", text="Lastname")
        tv.column("Lastname", anchor="center", width=100)
        tv.heading("4-SSN", text="4-SSN")
        tv.column("4-SSN", anchor="w", width=70)
        tv.grid(sticky=(N,S,W,E))
        self.treeview = tv

        #Create a scrollbar for treeview
        self.yscrollbar = ttk.Scrollbar(self, orient="vertical", command=tv.yview)
        tv.configure(yscrollcommand=self.yscrollbar.set)
        tv.grid(row=1, column=0, sticky="nsew")
        self.yscrollbar.grid(row=1, column=1, sticky="nse")
        self.yscrollbar.configure(command=tv.yview)

        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)


    
    def resetTreeview(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def loadTable(self, r):
        for i in r:
            acctID = i[0]
            routing = i[1]
            checking = i[2]
            SSN = i[3]
            firstname = i[4]
            lastname = i[5]
            self.treeview.insert("","end",text=acctID, values=(routing, checking,
                                                                 firstname, lastname, SSN))

        #self.treeview.insert("","end",text="AleWi", values=("Alex", "Williams",
                                                           #"282", "2017/5/22"))
        
    def createFilterPanel(self, parent):
        lbFirstname = Label(self, text = "Firstname")
        lbFirstname.grid(row=0, column=2)

        firstname_text = StringVar()
        tbFirstname = Entry(self, textvariable=firstname_text)
        tbFirstname.grid(row=0, column=3)

        lbLastname = Label(self, text = "Lastname")
        lbLastname.grid(row=0, column=4)

        Lastname_text = StringVar()
        tbLastname = Entry(self, textvariable=Lastname_text)
        tbLastname.grid(row=0, column=5)

        lbSSN = Label(self, text = "4-SSN")
        lbSSN.grid(row=1, column=2)

        SSN_text = StringVar()
        tbSSN = Entry(self, textvariable=SSN_text)
        tbSSN.grid(row=1, column=3)

        lbSortOption = Label(self, text = "Sort by: ")
        lbSortOption.grid(row=1, column=4)
        
        spinSortOption = StringVar()
        choices = ["--","--", "Routing#", "Firstname", "Lastname"]
        SortOptionMenu = OptionMenu(self, spinSortOption, *choices)
        SortOptionMenu.grid(row=1, column=5)
        spinSortOption.set(choices[0])

        btnSubmit = Button(self,
                           text="Search",
                           command=lambda: self.submitFilter(tbFirstname.get(), tbLastname.get(), tbSSN.get(), spinSortOption.get()))
        btnSubmit.grid(row=2, column=2)

        btnClear = Button(self,
                           text="Clear",
                           command=lambda: self.clearText(firstname_text, Lastname_text, SSN_text, spinSortOption, choices))
        btnClear.grid(row=2, column=3)

        btnClose = Button(self,
                           text="Close",
                           command=parent.destroy)
        btnClose.grid(row=2, column=4)


    def clearText(self, txtFirstname, txtLastname, txtSSN, sortoption, choices):
        txtFirstname.set("")
        txtLastname.set("")
        txtSSN.set("")
        sortoption.set(choices[0])

    def submitFilter(self, argFirstname, argLastname, argSSN, sortoption):
        global record
        q = queryBanking()
 
        
        if sortoption == "" or sortoption == "--":
            sortoption = "Lastname"
        elif sortoption == "AvgRating":
            sortoption = "avgStarRate"

        if not argFirstname == "" and argLastname == "":
            record = q.fetchbyfirstname(argFirstname, sortoption)
        elif argFirstname and argLastname:
                record = q.fetchbyname(argFirstname, argLastname, sortoption)
        elif argFirstname == "" and argLastname != "":
            record = q.fetchbylastname(argLastname, sortoption)
        elif argSSN and argFirstname or argLastname:
            if argFirstname:
                record = q.fetchSSFName(argSSN, argFirstname, sortoption)
            else:
                record = q.fetchSSLName(argSSN, argLastname, sortoption)
        elif argSSN and argFirstname == "" and argLastname == "":
            record = q.fetchSSN(argSSN, sortoption)
        else:
            record = q.fetchbankrecord(sortoption)
        self.resetTreeview()
        self.loadTable(record)


def main():
    root = Tk()
    bankTreeview(root)
    root.mainloop()


if __name__ == "__main__":
    main()
