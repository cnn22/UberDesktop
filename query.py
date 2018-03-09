import mysql.connector
from mysql.connector import errorcode

class Query():


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
          return table
      cnx.close()


  def fetchbyusername(self, username):
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
                                 AND u.username = '%s';"""%username)
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          return record
      cnx.close()

  def fetchbylastname(self, lastname):
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
                                 AND u.lastname = '%s';"""%lastname)
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          return record
      cnx.close()

  def fetchbyfirstname(self, firstname):
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
                                 AND u.firstname = '%s';"""%firstname)
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          return record
      cnx.close()

  def fetchbyname(self, firstname, lastname):
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
                                 AND u.lastname = '%s';"""%(firstname,lastname))
          #print(query)
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          return record
      cnx.close()

  def fetchincidentrecord(self):
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
                              AND d.username = u.username;""")
        cursor = cnx.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        return record;
    cnx.close()
