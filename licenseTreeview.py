from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from queryLicense import *

class driverLicenseView(Frame):

    record = ""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.createUI()
        self.createFilterPanel(parent)
        self.grid(sticky = (N,S,W,E))
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid(row=1, column=0)

    def createUI(self):
        tv = Treeview(self)
        tv['columns'] = ('Lastname', 'Firstname', 'Gender', 'DOB', 'IssueDate', 'ExpDate',
                         'Height', 'Weight','Eyecolor')
        tv.heading('#0', text='Licenses', anchor='w')
        tv.column('#0', anchor='w', width=100 )
        tv.heading('Lastname', text='Lastname')
        tv.column('Lastname', anchor='center', width=150)
        tv.heading('Firstname', text='Firstname')
        tv.column('Firstname', anchor='center', width=150)
        tv.heading('Gender', text='Gender')
        tv.column('Gender', anchor='center', width=75)
        tv.heading('DOB', text='DOB')
        tv.column('DOB', anchor='center', width=100)
        tv.heading('IssueDate', text='IssueDate')
        tv.column('IssueDate', anchor='center', width=150)
        tv.heading('ExpDate', text='ExpDate')
        tv.column('ExpDate', anchor='center', width=150)
        tv.heading('Height', text='Height')
        tv.column('Height', anchor='center', width=75)
        tv.heading('Weight', text='Weight')
        tv.column('Weight', anchor='center', width=75)
        tv.heading('Eyecolor', text='Eyecolor')
        tv.column('Eyecolor',anchor='center', width=75)
        tv.grid(sticky=(N,S,W,E))
        self.treeview = tv
        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=tv.yview)
        tv.configure(yscrollcommand=self.yscrollbar.set)

        tv.grid(row=1, column=0, sticky="nsew")
        self.yscrollbar.grid(row=1, column=1, sticky='nse')
        self.yscrollbar.configure(command=tv.yview)
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)


    def resetTreeview(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def loadTable(self, r):
        for i in r:
            licenseNum = i[0]
            lastname = i[1]
            firstname = i[2]
            gender = i[3]
            DOB = i[4]
            issueDate = i[5]
            expDate = i[6]
            height= i[7]
            weight = i[8]
            eyecolor  = i[9]
            self.treeview.insert('','end',text=licenseNum, values=(lastname, firstname,
                                                                 gender, DOB, issueDate, expDate,
                                                                 height, weight, eyecolor))

        #self.treeview.insert('','end',text='AleWi', values=('Alex', "Williams",
                                                           #'282', '2017/5/22'))
        
    def createFilterPanel(self, parent):
        lbFirstname = Label(self, text = 'Firstname')
        lbFirstname.grid(row=0, column=2)

        firstname_text = StringVar()
        tbFirstname = Entry(self, textvariable=firstname_text)
        tbFirstname.grid(row=0, column=3)

        lbLastname = Label(self, text = 'Lastname')
        lbLastname.grid(row=0, column=4)

        Lastname_text = StringVar()
        tbLastname = Entry(self, textvariable=Lastname_text)
        tbLastname.grid(row=0, column=5)

        lbLicense = Label(self, text = 'License#')
        lbLicense.grid(row=1, column=2)

        License_text = StringVar()
        tbLicense = Entry(self, textvariable=License_text)
        tbLicense.grid(row=1, column=3)

        lbSortOption = Label(self, text = 'Sort by: ')
        lbSortOption.grid(row=1, column=4)

        spinSortOption = StringVar()
        choices = {'--', 'License#', 'Firstname', 'Lastname', 'DOB', 'Gender',
                   'IssueDate', 'ExpDate', 'Height', 'Weight', 'Eyecolor'}
        spinSortOption.set('--')


        SortOptionMenu = OptionMenu(self, spinSortOption, *choices)
        SortOptionMenu.grid(row=1, column=5)

        btnSubmit = Button(self,
                           text='Search',
                           command=lambda: self.submitFilter(tbFirstname.get(), tbLastname.get(), tbLicense.get(), spinSortOption.get()))
        btnSubmit.grid(row=2, column=2)

        btnClear = Button(self,
                           text='Clear',
                           command=lambda: self.clearText(firstname_text, Lastname_text, License_text, spinSortOption))
        btnClear.grid(row=2, column=3)

        btnClose = Button(self,
                           text='Close',
                           command=parent.destroy)
        btnClose.grid(row=2, column=4)


    def clearText(self, txtFirstname, txtLastname, txtLicense, sortoption):
        txtFirstname.set("")
        txtLastname.set("")
        txtLicense.set("")
        sortoption.set("")

    def submitFilter(self, argFirstname, argLastname, argLicense, sortoption):
        global record
        q = QueryLicense()
        if sortoption == "":
            sortoption = "Lastname"

        if not argFirstname == "" and argLastname == "":
            record = q.fetchbyfirstname(argFirstname, sortoption)
        elif argFirstname and argLastname:
                record = q.fetchbyname(argFirstname, argLastname, sortoption)
        elif argLicense:
            record = q.fetchbylicense(argLicense, sortoption)

        if argLastname and argFirstname == "":
            record = q.fetchbylastname(argLastname, sortoption)


        if argFirstname == "" and argLastname == "" and argLicense == "":
            record = q.fetchlicenserecord(sortoption)

        #if not argUsername == "":
            #record = q.fetchbyusername(argUsername)
        self.resetTreeview()
        self.loadTable(record)


def main():
    root = Tk()
    driverLicenseView(root)
    root.mainloop()


if __name__ == '__main__':
    main()
