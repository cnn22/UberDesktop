import mysql.connector
from mysql.connector import errorcode

class AddressQuery():

    #used to help us sort the Address data in the database in a certain way
    def formatsort(self, sortoption):
        if sortoption == "Username":
            sortoption = "u.username"
            return sortoption
        elif sortoption == "Firstname":
            sortoption = "u.firstname"
            return sortoption
        elif sortoption == "Lastname":
            sortoption = "u.lastname"
            return sortoption

    #fetches the address table
    def fetchtable(self):
        try:
            cnx = mysql.connector.connect(user='root', password='1eC8E$NT*b', host = '127.0.0.1', database='uber')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
            elif err.errno == errorcode.ER_BAD_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            #print(query)
            cursor = cnx.cursor()
            cursor.execute("USE uber")
            cursor.execute("SHOW TABLES")
            record = cursor.fetchall()
            cnx.close()
            return record

    def fetchbyusername(self, username, sortoption):
        try:
            cnx = mysql.connector.connect(user='root', password='1eC8E$NT*b', host = '127.0.0.1', database='uber')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
            elif err.errno == errorcode.ER_BAD_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            sortoption = self.formatsort(sortoption)
            query = ("""SELECT
                        u.username, u.firstname, u.lastname, a.addressName, a.streetName, a.aptNum, a.city, a.zipcode
                        FROM uberaccount u, address a
                        WHERE
                        a.username = u.username AND
                        u.username = '%s'
                        ORDER BY %s;"""%(username, sortoption))

            cursor = cnx.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            cnx.close()
            return record

    def fetchAddressTable(self, sortoption):
        try:
            cnx = mysql.connector.connect(user='root', password='1eC8E$NT*b', host = '127.0.0.1', database='uber')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
            elif err.errno == errorcode.ER_BAD_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            sortoption = self.formatsort(sortoption)
            query = ("""SELECT u.username, u.firstname, u.lastname, a.addressName, a.streetName, a.aptNum, a.city, a.zipcode
                        FROM uberaccount u, address a
                        WHERE u.username = a.username
                        ORDER BY %s;"""%(sortoption))
            cursor = cnx.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            cnx.close()
            return record


def main():
    b = AddressQuery()
    print(b.fetchtable())

if __name__ =='__main__':
    main()
