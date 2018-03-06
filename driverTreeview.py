from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from query import *

class driverRecord(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.createUI()
        self.loadTable()
        self.grid(sticky = (N,S,W,E))
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid(row=1, column=0)

    def createUI(self):
        tv = Treeview(self)        
        tv['columns'] = ('Firstname', 'Lastname', 'TicketID', 'Date')
        tv.heading('#0', text='Username', anchor='w')
        tv.column('#0', anchor='w')
        tv.heading('Firstname', text='Firstname')
        tv.column('Firstname', anchor='center', width=150)
        tv.heading('Lastname', text='Lastname')
        tv.column('Lastname', anchor='center', width=150)
        tv.heading('TicketID', text='TicketID')
        tv.column('TicketID', anchor='center', width=150)
        tv.heading('Date', text='Date')
        tv.column('Date', anchor='center', width=150)
        tv.grid(sticky=(N,S,W,E))
        self.treeview = tv
        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=tv.yview)
        tv.configure(yscrollcommand=self.yscrollbar.set)

        tv.grid(row=0, column=0, sticky="nsew")
        self.yscrollbar.grid(row=0, column=1, sticky='nse')
        self.yscrollbar.configure(command=tv.yview)
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight = 1)

    def loadTable(self):
        q = Query()
        record = q.fetchincidentrecord()

        for i in record:
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
    lbFirstname.grid(row=0, column=1)

    firstname_text = StringVar()
    tbFirstname = Entry(self, textvariable=firstname_text)
    tbFirstname.grid(row=0, column=2)

    lbLastname = Label(self, text = 'Lastname')
    lbLastname.grid(row=0, column=3)

    Lastname_text = StringVar()
    tbLastname = Entry(self, textvariable=Lastname_text)
    tbLastname.grid(row=0, column=4)

    lbUsername = Label(self, text = 'Username')
    lbUsername.grid(row=1, column=1)

    Username_text = StringVar()
    tbUsername = Entry(self, textvariable=Username_text)
    tbUsername.grid(row=1, column=2)

    
    
def main():
    root = Tk()
    createFilterPanel(root)
    driverRecord(root)
    root.mainloop()


if __name__ == '__main__':
    main()


#scrollbar = Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)
