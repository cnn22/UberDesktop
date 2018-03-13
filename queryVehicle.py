import mysql.connector
from mysql.connector import errorcode

class VehicleQuery():

    #used to help us sort the Vehicle data in the database in a certain way
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
        elif sortoption == "LicensePlate":
            sortoption = "v.licensePlate"
            return sortoption
        elif sortoption == "Year":
            sortoption ="v.Year"
            return sortoption

    #fetches the Vehicle table
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
                        d.driverid, u.username, u.firstname, u.lastname, v.carid, v.licenseplate, v.color, v.year, v.model, v.numseats
                        FROM uberaccount u, driver d, vehicle v
                        WHERE
                        u.username = d.username and d.driverid = v.driverid
                        u.username = '%s'
                        ORDER BY %s;"""%(username, sortoption))

            cursor = cnx.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            cnx.close()
            return record

    def fetchbydriverID(self, driverID, sortOption):
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
            sortoption = self.formatsort(sortOption)
            query = ("""SELECT d.driverid, u.username, u.firstname, u.lastname, v.carid, v.licenseplate, v.color, v.year, v.model, v.numseats
                        FROM uberaccount u, driver d, vehicle v
                        WHERE u.username = d.username and d.driverid = v.driverid
                        ORDER BY %S;"""%(licensePlate, sortoption)
                    )
            cursor = cnx.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            cnx.close()
            return record

    def fetchbyYear(self, year, sortoption):
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
            sortoption = self.formatsort(sortOption)
            query = ("""SELECT d.driverid, u.username, u.firstname, u.lastname, v.carid, v.licenseplate, v.color, v.year, v.model, v.numseats
                        FROM uberaccount u, driver d, vehicle v
                        WHERE u.username = d.username and d.driverid = v.driverid
                        ORDER BY %s;"""%(year, sortoption)
                    )
            cursor = cnx.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            cnx.close()
            return record

    def fetchVehicleTable(self, sortoption):
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
            query = ("""SELECT d.driverid, u.username, u.firstname, u.lastname, v.carid, v.licenseplate, v.color, v.year, v.model, v.numseats
                        FROM uberaccount u, driver d, vehicle v
                        WHERE u.username = d.username and d.driverid = v.driverid
                        ORDER BY %s;"""%(sortoption))
            cursor = cnx.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            cnx.close()
            return record

def main():
    b = VehicleQuery()
    #print(b.fetchtable())

if __name__ =='__main__':
    main()
