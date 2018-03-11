from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from queryRating import *

class userRating(Frame):

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
        tv["columns"] = ("Lastname", "Firstname", "AvgRating", "Comment", "Indicator")
        tv.heading("#0", text="Username", anchor="w")
        tv.column("#0", anchor="w", width=75 )
        tv.heading("Lastname", text="Lastname")
        tv.column("Lastname", anchor="center", width=150)
        tv.heading("Firstname", text="Firstname")
        tv.column("Firstname", anchor="center", width=150)
        tv.heading("AvgRating", text="AvgRating")
        tv.column("AvgRating", anchor="center", width=70)
        tv.heading("Comment", text="Comment")
        tv.column("Comment", anchor="center", width=100)
        tv.heading("Indicator", text="Indicator")
        tv.column("Indicator", anchor="w", width=70)
        tv.grid(sticky=(N,S,W,E))
        self.treeview = tv
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
            username = i[0]
            lastname = i[1]
            firstname = i[2]
            avgRating = i[3]
            comment = i[4]
            if comment == None:
                comment =""
            indicator = i[5]
            if indicator == 0:
                indicator = "Rider"
            else:
                indicator = "Driver"
            self.treeview.insert("","end",text=username, values=(lastname, firstname,
                                                                 avgRating, comment, indicator))

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

        lbIndicator = Label(self, text = "Indicator")
        lbIndicator.grid(row=1, column=2)

        IndicateOption = ["--", "Driver", "Rider"]
        indicatorOpt = StringVar()
        indicatorOptionMenu = OptionMenu(self, indicatorOpt, *IndicateOption)
        indicatorOptionMenu.grid(row=1, column=3)
        indicatorOpt.set(IndicateOption[0])

        lbSortOption = Label(self, text = "Sort by: ")
        lbSortOption.grid(row=1, column=4)
        
        spinSortOption = StringVar()
        choices = ["--", "Username", "Firstname", "Lastname", "AvgRating",
                   "Indicator"]
        SortOptionMenu = OptionMenu(self, spinSortOption, *choices)
        SortOptionMenu.grid(row=1, column=5)
        spinSortOption.set(choices[0])

        btnSubmit = Button(self,
                           text="Search",
                           command=lambda: self.submitFilter(tbFirstname.get(), tbLastname.get(), indicatorOpt.get(), spinSortOption.get()))
        btnSubmit.grid(row=2, column=2)

        btnClear = Button(self,
                           text="Clear",
                           command=lambda: self.clearText(firstname_text, Lastname_text, indicatorOpt, spinSortOption))
        btnClear.grid(row=2, column=3)

        btnClose = Button(self,
                           text="Close",
                           command=parent.destroy)
        btnClose.grid(row=2, column=4)


    def clearText(self, txtFirstname, txtLastname, indicatorOpt, sortoption):
        txtFirstname.set("")
        txtLastname.set("")
        indicatorOpt.set("")
        sortoption.set("")

    def submitFilter(self, argFirstname, argLastname, argIndicator, sortoption):
        global record
        q = queryRating()
 
        
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
        elif argIndicator:
            if not argIndicator == "--":
                if argIndicator == "Driver":
                    argIndicator = 1
                elif argIndicator == "Rider":
                    argIndicator = 0
                record = q.fetchbyindicator(argIndicator, sortoption)
            else:
                record = q.fetchratingrecord(sortoption)
        else:
            record = q.fetchratingrecord(sortoption)
        self.resetTreeview()
        self.loadTable(record)


def main():
    root = Tk()
    userRating(root)
    root.mainloop()


if __name__ == "__main__":
    main()
