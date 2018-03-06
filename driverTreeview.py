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

def main():
    root = Tk()
    driverRecord(root)
    root.mainloop()


if __name__ == '__main__':
    main()


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
