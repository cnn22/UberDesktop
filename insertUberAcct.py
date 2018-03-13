from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import mysql.connector
from mysql.connector import errorcode

fields = "username","firstname","lastname","secret","email","phoneNum","driverOpt"  
class insert():
    def insertAccount(self, statement):        
        insertTest = "INSERT INTO uberaccount(username,firstname,lastname,secret,email,phoneNum,driverOpt) VALUES('%s','%s','%s','%s','%s','%s','%s')" % (statement)
        try:
            cnx = mysql.connector.connect(user="Cortana", password="sqlpro2018", host= "uber.cqqmzgtyi8vj.us-east-1.rds.amazonaws.com",database="Uber")           
        except:
            cnx.rollback()
        cursor = cnx.cursor()
        cursor.execute(insertTest)
        cnx.commit()
        print("Success!")
        cnx.close()

#method to grab user entries
def fetch(entries):
    accountValues = []
    for entry in entries:
        accountValues.append(entry[1].get())
    retValues = tuple(accountValues)
    return retValues
    
                      
def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries


if __name__ == '__main__':
   root = Tk()
   i = insert()
   ents = makeform(root, fields)
   b1 = Button(root, text='Insert', command=(lambda e=ents: i.insertAccount(fetch(e))) )
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
   
