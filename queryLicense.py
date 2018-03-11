"""
List of all Functions:


"""

import mysql.connector
from mysql.connector import errorcode

class QueryLicense():

  def formatsort(self, sortoption):
      if sortoption == "License#":
        sortoption = "dl.licenseNum"
        return sortoption
      elif sortoption == "ExpDate":
        sortoption = "dl.expirationDate"
        return sortoption
      elif (sortoption == "Firstname" or sortoption == "Lastname"):
        sortoption = "u.%s"%sortoption
        return sortoption
      else:
        sortoption = "dl.%s"%sortoption
        return sortoption

  def fetchbylicense(self, licenses, sortoption):
      try:
          cnx = mysql.connector.connect(user='root', password='root', host = '127.0.0.1',
                                       database='test')
      except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
              print("Database does not exist")
          else:
              print(err)
      else:
          sortoption = self.formatsort(sortoption)
          query = ("""SELECT 
                          dl.licenseNum,
                          u.lastname,
                          u.firstname,
                          dl.gender,
                          dl.DOB,
                          dl.issueDate,
                          dl.expirationDate,
                          dl.height,
                          dl.weight,
                          dl.eyeColor
                      FROM
                          driverlicense dl,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = dl.driverid
                              AND u.username = d.username
                              AND dl.licenseNum = '%s'
                              ORDER BY %s;"""%(licenses, sortoption))
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record


  def fetchbylastname(self, lastname, sortoption):
      try:
          cnx = mysql.connector.connect(user='root', password='root', host = '127.0.0.1',
                                       database='test')
      except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
              print("Database does not exist")
          else:
              print(err)
      else:
          sortoption = self.formatsort(sortoption)
          query = ("""SELECT 
                          dl.licenseNum,
                          u.lastname,
                          u.firstname,
                          dl.gender,
                          dl.DOB,
                          dl.issueDate,
                          dl.expirationDate,
                          dl.height,
                          dl.weight,
                          dl.eyeColor
                      FROM
                          driverlicense dl,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = dl.driverid
                              AND u.username = d.username
                              AND u.lastname = '%s'
                              ORDER BY %s;"""%(lastname, sortoption))
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record


  def fetchbyfirstname(self, firstname, sortoption):
      try:
          cnx = mysql.connector.connect(user='root', password='root', host = '127.0.0.1',
                                       database='test')
      except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
              print("Database does not exist")
          else:
              print(err)
      else:
          sortoption = self.formatsort(sortoption)
          query = ("""SELECT 
                          dl.licenseNum,
                          u.lastname,
                          u.firstname,
                          dl.gender,
                          dl.DOB,
                          dl.issueDate,
                          dl.expirationDate,
                          dl.height,
                          dl.weight,
                          dl.eyeColor
                      FROM
                          driverlicense dl,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = dl.driverid
                              AND u.username = d.username
                              AND u.firstname = '%s'
                              ORDER BY %s;"""%(firstname, sortoption))
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record

  def fetchlicenserecord(self, sortoption):
      try:
        cnx = mysql.connector.connect(user='root', password='root', host = '127.0.0.1',
                                        database='test')
      except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
          print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
          print("Database does not exist")
        else:
          print(err)
      else:
          sortoption = self.formatsort(sortoption)
          query = ("""SELECT
                            dl.licenseNum,
                            u.lastname,
                            u.firstname,
                            dl.gender,
                            dl.DOB,
                            dl.issueDate,
                            dl.expirationDate,
                            dl.height,
                            dl.weight,
                            dl.eyeColor
                        FROM
                            driverlicense dl,
                            uberaccount u,
                            driver d
                        WHERE
                            d.driverid = dl.driverid
                                AND u.username = d.username
                                ORDER BY %s;"""%(sortoption))
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record;
