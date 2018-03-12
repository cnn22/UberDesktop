"""
List of all Functions:


"""

import mysql.connector
from mysql.connector import errorcode

class queryBanking():

  def formatsort(self, sortoption):
      if sortoption == "Firstname" or sortoption == "Lastname":
        sortoption = "u.%s"%sortoption
        return sortoption
      else:
        if sortoption == "Routing#":
          sortoption = "b.routingNum"
        else:
          sortoption = "b.%s"%sortoption
        return sortoption

  def fetchSSLName(self, argSSN, argLName, sortoption):
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
                          b.accountID,
                          b.routingNum,
                          b.checkingNum,
                          b.lastFourSSN,
                          u.firstname,
                          u.lastname
                      FROM
                          bankingaccount b,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = b.driverid
                              AND u.username = d.username
                              AND u.lastname = '%s'
                              AND b.lastFourSSN = '%s'
                      ORDER BY %s;"""%(argLName, argSSN, sortoption))
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record

  def fetchSSFName(self, argSSN, argFName, sortoption):
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
                          b.accountID,
                          b.routingNum,
                          b.checkingNum,
                          b.lastFourSSN,
                          u.firstname,
                          u.lastname
                      FROM
                          bankingaccount b,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = b.driverid
                              AND u.username = d.username
                              AND u.firstname = '%s'
                              AND b.lastFourSSN = '%s'
                      ORDER BY %s;"""%(argFName, argSSN, sortoption))
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
                          b.accountID,
                          b.routingNum,
                          b.checkingNum,
                          b.lastFourSSN,
                          u.firstname,
                          u.lastname
                      FROM
                          bankingaccount b,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = b.driverid
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
                          b.accountID,
                          b.routingNum,
                          b.checkingNum,
                          b.lastFourSSN,
                          u.firstname,
                          u.lastname
                      FROM
                          bankingaccount b,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = b.driverid
                              AND u.username = d.username
                              AND u.firstname = '%s'
                      ORDER BY %s;"""%(firstname, sortoption))
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record

  def fetchSSN(self, argSSN, sortoption):
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
                          b.accountID,
                          b.routingNum,
                          b.checkingNum,
                          b.lastFourSSN,
                          u.firstname,
                          u.lastname
                      FROM
                          bankingaccount b,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = b.driverid
                              AND u.username = d.username
                              AND b.lastFourSSN = '%s'
                      ORDER BY %s;"""%(argSSN, sortoption))
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record;

  def fetchbankrecord(self, sortoption):
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
                          b.accountID,
                          b.routingNum,
                          b.checkingNum,
                          b.lastFourSSN,
                          u.firstname,
                          u.lastname
                      FROM
                          bankingaccount b,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverid = b.driverid
                              AND u.username = d.username
                      ORDER BY %s;"""%(sortoption))
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record;
