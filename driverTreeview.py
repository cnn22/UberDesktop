from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from query import *

class driverRecord(Frame):

    record = ""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.createUI()
        self.createFilterPanel()
        self.fetchallincidentrecord()
        self.grid(sticky = (N,S,W,E))
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid(row=1, column=0)

    def createUI(self):
        tv = Treeview(self)        
        tv['columns'] = ('Firstname', 'Lastname', 'TicketID', 'Date')
        tv.heading('#0', text='Username', anchor='w')
        tv.column('#0', anchor='w', width=150 )
        tv.heading('Firstname', text='Firstname')
        tv.column('Firstname', anchor='center', width=150)
        tv.heading('Lastname', text='Lastname')
        tv.column('Lastname', anchor='center', width=150)
        tv.heading('TicketID', text='TicketID')
        tv.column('TicketID', anchor='center', width=100)
        tv.heading('Date', text='Date')
        tv.column('Date', anchor='center', width=150)
        tv.grid(sticky=(N,S,W,E))
        self.treeview = tv
        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=tv.yview)
        tv.configure(yscrollcommand=self.yscrollbar.set)

        tv.grid(row=1, column=0, sticky="nsew")
        self.yscrollbar.grid(row=1, column=1, sticky='nse')
        self.yscrollbar.configure(command=tv.yview)
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)
        

    def fetchallincidentrecord(self):
        global record
        q = Query()
        record = q.fetchincidentrecord()
        self.loadTable(record)

    def resetTreeview(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def loadTable(self, r):
        for i in r:
            username = i[0]
            firstname = i[1]
            lastname = i[2]
            ticketID = i[3]
            date = i[4]
            self.treeview.insert('','end',text=username, values=(firstname,lastname,
                                                                 ticketID,date))
        
        #self.treeview.insert('','end',text='AleWi', values=('Alex', "Williams",
                                                           #'282', '2017/5/22'))
        
    def createFilterPanel(self):
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

        lbUsername = Label(self, text = 'Username')
        lbUsername.grid(row=1, column=2)

        Username_text = StringVar()
        tbUsername = Entry(self, textvariable=Username_text)
        tbUsername.grid(row=1, column=3)

        lbSortOption = Label(self, text = 'Sort by: ')
        lbSortOption.grid(row=1, column=4)

        spinSortOption = StringVar()
        choices = {'', 'Username', 'Firstname', 'Lastname', 'TicketID', 'Date'}
        

        SortOptionMenu = OptionMenu(self, spinSortOption, *choices)
        SortOptionMenu.grid(row=1, column=5)

        btnSubmit = Button(self,
                           text='Search',
                           command=lambda: self.submitFilter(tbFirstname.get(), tbLastname.get(), tbUsername.get()))
        btnSubmit.grid(row=2, column=2)
        
        btnClear = Button(self,
                           text='Clear',
                           command=lambda: self.clearText(firstname_text, Lastname_text, Username_text))
        btnClear.grid(row=2, column=3)


    def clearText(self, txtFirstname, txtLastname, txtUsername):
        txtFirstname.set("")
        txtLastname.set("")
        txtUsername.set("")

    def submitFilter(self, argFirstname, argLastname, argUsername):
        global record
        q = Query()
        
        if not argFirstname == "" and argLastname == "":
            record = q.fetchbyfirstname(argFirstname)
        elif argFirstname and argLastname:
                record = q.fetchbyname(argFirstname, argLastname)
        elif argUsername:
            record = q.fetchbyusername(argUsername)

        if argLastname and argFirstname == "":
            record = q.fetchbylastname(argLastname)


        if argFirstname == "" and argLastname == "" and argUsername == "":
            self.fetchallincidentrecord()

        #if not argUsername == "":
            #record = q.fetchbyusername(argUsername)
            
        self.resetTreeview()
        self.loadTable(record)

    
def main():
    root = Tk()
    driverRecord(root)
    root.mainloop()


if __name__ == '__main__':
    main()

