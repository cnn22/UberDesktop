"""
List of all Functions:


"""

import mysql.connector
from mysql.connector import errorcode

class queryRating():

  def formatsort(self, sortoption):
      if sortoption == "Firstname" or sortoption == "Lastname":
        sortoption = "u.%s"%sortoption
        return sortoption
      else:
        sortoption = "ur.%s"%sortoption
        return sortoption

  def fetchbyindicator(self, indicator, sortoption):
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
                          ur.username,
                          u.lastname,
                          u.firstname,
                          ur.avgStarRate,
                          ur.RatingComment,
                          ur.indicator
                      FROM
                          uberaccount u,
                          userrating ur
                      WHERE
                          ur.username = u.username
                              AND ur.indicator = %s
                              ORDER BY %s;"""%(indicator, sortoption))
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
                          ur.username,
                          u.lastname,
                          u.firstname,
                          ur.avgStarRate,
                          ur.RatingComment,
                          ur.indicator
                      FROM
                          uberaccount u,
                          userrating ur
                      WHERE
                          ur.username = u.username
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
                          ur.username,
                          u.lastname,
                          u.firstname,
                          ur.avgStarRate,
                          ur.RatingComment,
                          ur.indicator
                      FROM
                          uberaccount u,
                          userrating ur
                      WHERE
                          ur.username = u.username
                              AND u.firstname = '%s'
                      ORDER BY %s;"""%(firstname, sortoption))
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record

  def fetchratingrecord(self, sortoption):
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
                          ur.username,
                          u.lastname,
                          u.firstname,
                          ur.avgStarRate,
                          ur.RatingComment,
                          ur.indicator
                      FROM
                          uberaccount u,
                          userrating ur
                      WHERE
                          ur.username = u.username
                          ORDER BY %s;"""%(sortoption))
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record;
