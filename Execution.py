class Execution():


    def mysqlExecute(self, username, password, host, dbname, query):
      try:
          cnx = mysql.connector.connect(user=username, password=password, host = host,
                                       database=dbname)
      except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
              print("Database does not exist")
          else:
              print(err)
      else:
          cursor = cnx.cursor()
          cursor.execute(query)
          record = cursor.fetchall()
          cnx.close()
          return record
