from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from queryVehicle import *

class vehicleRecord(Frame):
    record = ""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.vehicleUI()
        self.createFilterPanel(parent)
        self.grid(sticky = (N,S,W,E))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=1, column=0)

    def vehicleUI(self):
        tv = Treeview(self)
        tv['columns'] = ("Username", "Firstname", "Lastname", "CarID", "LicensePlate", "Year", "Color", "Model", "NumSeats")
        tv.heading("#0", text="DriverID", anchor='w')
        tv.column("#0", anchor='w', width=50)

        tv.heading("Username",text="Username")
        tv.column("Username", anchor="center", width=60)

        tv.heading("Firstname",text="Firstname")
        tv.column("Firstname", anchor="center", width=60)

        tv.heading("Lastname", text="Lastname")
        tv.column("Lastname", anchor="center", width=60)

        tv.heading("CarID", text="CarID")
        tv.column("CarID", anchor="center", width=40)

        tv.heading("LicensePlate", text="LicensePlate")
        tv.column("LicensePlate", anchor="center", width=75)

        tv.heading("Year", text="Year")
        tv.column("Year", anchor="center", width=35)

        tv.heading("Color", text="Color")
        tv.column("Color", anchor="center", width=38)

        tv.heading("Model", text="Model")
        tv.column("Model", anchor="center", width=50)

        tv.heading("NumSeats", text="NumSeats")
        tv.column("NumSeats", anchor="center", width=55)

        #tv.heading("VehicleTypeID", text="VehicleTypeID")
        #tv.column("VehicleTypeID", anchor="center", width=60)
        tv.grid(sticky=(N,S,W,E))
        self.treeview = tv
        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=tv.yview)
        tv.configure(yscrollcommand=self.yscrollbar.set)

        tv.grid(row=1, column=0, sticky="nsew")
        self.yscrollbar.grid(row=1, column=1, sticky="nse")
        self.yscrollbar.configure(command=tv.yview)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0, weight=1)

    def fetchallVehicles(self, sortoption):
        global record
        q = VehicleQuery()
        record = q.fetchVehicleTable(sortoption)
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
        choices = {"Username", "Firstname", "Lastname", "License Plate", "Year"}

        SortOptionMenu = OptionMenu(self, spinSortOption, *choices)
        SortOptionMenu.grid(row=1, column=5)

        btnSubmit = Button(self, text="Search", command=lambda:self.submitFilter(tbFirstname.get(), tbLastname.get(), tbUsername.get(), spinSortOption.get()))
        btnSubmit.grid(row=2, column=4)

        btnClear = Button(self, text="Clear", command=lambda:self.clearText(firstname_text, Lastname_text, Username_text, spinSortOption))
        btnClear.grid(row=2, column=3)

        btnClose = Button(self, text='Close', command=parent.destroy)
        btnClose.grid(row=2, column=5)

    def fetchVehicleTable(self, sortoption):
        global record
        q=VehicleQuery()
        record = q.fetchVehicleTable(sortoption)
        self.loadTable(record)

    def clearText(self, txtFirstname, txtLastname, txtUsername, sortoption):
        txtFirstname.set("")
        txtLastname.set("")
        txtUsername.set("")
        sortoption.set("")

    def submitFilter(self, argFirstname, argLastname, argUsername, sortOption):
        global record
        q = VehicleQuery()
        if sortOption == "":
            sortOption = "Username"

        if argFirstname == "" and argLastname == "" and argUsername == "":
            self.fetchVehicleTable(sortOption)

        self.resetTreeview()
        self.loadTable(record)

    def loadTable(self, r):
        for i in r:
            driverID = i[0]
            username = i[1]
            firstname = i[2]
            lastname = i[3]
            carID = i[4]
            licensePlate = i[5]
            color = i[6]
            year = i[7]
            model = i[8]
            numSeats = i[9]
            #vehicleTypeID = i[]
            self.treeview.insert('', 'end', text=driverID, values=(username, firstname, lastname, carID, licensePlate, color, year, model, numSeats))

def main():
    root=Tk()
    vehicleRecord(root)
    root.mainloop()

if __name__=="__main__":
    main()
