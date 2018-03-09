"""
List of all Functions:
fetchbyusername(self, username)
fetchbylastname(self, lastname)
fetchbyfirstname(self, firstname)
fetchbyname(self, firstname, lastname)
fetchincidentrecord(self)
fetchtablename(self)
formatsort(self, sortoption)

"""

import mysql.connector
from mysql.connector import errorcode

class Query():

  def formatsort(self, sortoption):
      if sortoption == "Date":
        sortoption = "ir.dateTimeIncident"
        return sortoption
      elif sortoption == "TicketID":
        sortoption = "ir.%s"%sortoption
        return sortoption
      if not (sortoption == "Date" or sortoption == "TicketID"):
        sortoption = "u.%s"%sortoption
        return sortoption
    
  def fetchtablename(self):
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
          cursor = cnx.cursor()
          cursor.execute("USE test")
          cursor.execute("SHOW TABLES")
          table = cursor.fetchall()
          cnx.close()
          return table

  def fetchbyusername(self, username, sortoption):
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
                             u.username,
                             u.firstname,
                             u.lastname,
                             ir.ticketID,
                             ir.dateTimeIncident
                         FROM
                             incidentrecord ir,
                             uberaccount u,
                             driver d
                         WHERE
                             d.driverID = ir.driverID
                                 AND d.username = u.username
                                 AND u.username = '%s'
                                 ORDER BY %s;"""%(username, sortoption))
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
                             u.username,
                             u.firstname,
                             u.lastname,
                             ir.ticketID,
                             ir.dateTimeIncident
                         FROM
                             incidentrecord ir,
                             uberaccount u,
                             driver d
                         WHERE
                             d.driverID = ir.driverID
                                 AND d.username = u.username
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
                             u.username,
                             u.firstname,
                             u.lastname,
                             ir.ticketID,
                             ir.dateTimeIncident
                         FROM
                             incidentrecord ir,
                             uberaccount u,
                             driver d
                         WHERE
                             d.driverID = ir.driverID
                                 AND d.username = u.username
                                 AND u.firstname = '%s'
                                 ORDER BY %s;"""%(firstname, sortoption))
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record
      

  def fetchbyname(self, firstname, lastname, sortoption):
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
                             u.username,
                             u.firstname,
                             u.lastname,
                             ir.ticketID,
                             ir.dateTimeIncident
                         FROM
                             incidentrecord ir,
                             uberaccount u,
                             driver d
                         WHERE
                             d.driverID = ir.driverID
                                 AND d.username = u.username
                                 AND u.firstname = '%s'
                                 AND u.lastname = '%s'
                                 ORDER BY %s;"""%(firstname,lastname, sortoption))
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record
      

  def fetchincidentrecord(self, sortoption):
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
                          u.username,
                          u.firstname,
                          u.lastname,
                          ir.ticketID,
                          ir.dateTimeIncident
                      FROM
                          incidentrecord ir,
                          uberaccount u,
                          driver d
                      WHERE
                          d.driverID = ir.driverID
                              AND d.username = u.username
                              ORDER BY %s;"""%(sortoption))
        cursor = cnx.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        cnx.close()
        return record;
    
