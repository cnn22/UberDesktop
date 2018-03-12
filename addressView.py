from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from addressQuery import *

class addressRecord(Frame):
    record = ""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.addressUI()
        self.createFilterPanel(parent)
        self.grid(sticky = (N,S,W,E))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=1, column=0)

    def addressUI(self):
        tv = Treeview(self)
        tv['columns'] = ("Firstname", "Lastname", "AddressName", "StreetName", "AptNum", "City", "Zipcode")
        tv.heading("#0", text="Username", anchor='w')
        tv.column("#0", anchor='w', width=70)

        tv.heading("Firstname",text="Firstname")
        tv.column("Firstname", anchor="center", width=60)

        tv.heading("Lastname", text="Lastname")
        tv.column("Lastname", anchor="center", width=60)

        tv.heading("AddressName", text="AddressName")
        tv.column("AddressName", anchor="center", width=75)

        tv.heading("StreetName", text="StreetName")
        tv.column("StreetName", anchor="center", width=75)

        tv.heading("AptNum", text="AptNum")
        tv.column("AptNum", anchor="center", width=55)

        tv.heading("City", text="City")
        tv.column("City", anchor="center", width=30)

        tv.heading("Zipcode", text="Zipcode")
        tv.column("Zipcode", anchor="center", width=50)
        tv.grid(sticky=(N,S,W,E))
        self.treeview = tv
        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=tv.yview)
        tv.configure(yscrollcommand=self.yscrollbar.set)

        tv.grid(row=1, column=0, sticky="nsew")
        self.yscrollbar.grid(row=1, column=1, sticky="nse")
        self.yscrollbar.configure(command=tv.yview)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0, weight=1)

    def fetchallAddresses(self, sortoption):
        global record
        q = addressQuery()
        record = q.fetchAddressTable(sortoption)
        self.loadtable(record)

    def resetTreeview(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def createFilterPanel(self, parent):
        lbFirstname = Label(self, text="Firstname")
        lbFirstname.grid(row=0, column=2)

        firstname_text = StringVar()
        tbFirstname = Entry(self, textvariable=firstname_text)
        tbFirstname.grid(row=0, column=3)

        lbLastname = Label(self, text="Lastname")
        lbLastname.grid(row=0, column=4)

        Lastname_text = StringVar()
        tbLastname = Entry(self, textvariable=Lastname_text)
        tbLastname.grid(row=0, column=5)

        lbUsername = Label(self, text="Username")
        lbUsername.grid(row=1, column=2)

        Username_text = StringVar()
        tbUsername = Entry(self, textvariable=Username_text)
        tbUsername.grid(row=1, column=3)

        lbSortOption = Label(self, text="Sort by: ")
        lbSortOption.grid(row=1, column=4)

        spinSortOption = StringVar()
        choices = {"Username", "Firstname", "Lastname"}

        SortOptionMenu = OptionMenu(self, spinSortOption, *choices)
        SortOptionMenu.grid(row=1, column=5)

        btnSubmit = Button(self, text="Search", command=lambda:self.submitFilter(tbFirstname.get(), tbLastname.get(), tbUsername.get(), spinSortOption.get()))
        btnSubmit.grid(row=2, column=4)

        btnClear = Button(self, text="Clear", command=lambda:self.clearText(firstname_text, Lastname_text, Username_text, spinSortOption))
        btnClear.grid(row=2, column=3)

        btnClose = Button(self, text='Close', command=parent.destroy)
        btnClose.grid(row=2, column=5)

    def fetchAddressTable(self, sortoption):
        global record
        q=AddressQuery()
        record = q.fetchAddressTable(sortoption)
        self.loadTable(record)

    def clearText(self, txtFirstname, txtLastname, txtUsername, sortoption):
        txtFirstname.set("")
        txtLastname.set("")
        txtUsername.set("")
        sortoption.set("")

    def submitFilter(self, argFirstname, argLastname, argUsername, sortOption):
        global record
        q = AddressQuery()
        if sortOption == "":
            sortOption = "Username"

        if argFirstname == "" and argLastname == "" and argUsername == "":
            self.fetchAddressTable(sortOption)

        self.resetTreeview()
        self.loadTable(record)

    def loadTable(self, r):
        for i in r:
            username = i[0]
            firstname = i[1]
            lastname = i[2]
            addressName = i[3]
            streetName = i[4]
            city = i[5]
            zipcode = i[6]
            self.treeview.insert('', 'end', text=username, values=(firstname, lastname, addressName, streetName, city, zipcode))

def main():
    root=Tk()
    addressRecord(root)
    root.mainloop()

if __name__=="__main__":
    main()
