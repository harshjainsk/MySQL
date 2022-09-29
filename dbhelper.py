import mysql.connector


class DBhelper:

    def __init__(self):

        """
            host : IP address of server,
            user and password are for accessing the database,
            database : name of the database you want to access
        """

        """
            We have created self.conn so that we do not login multiple times
            once self.conn  is created, my_cursor is used for communication with the database.
        """

        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password='123456', database="tutorial-campusx")
            self.my_cursor = self.conn.cursor()
        except Exception as e:
            print(e)
        else:
            print("Connected to database")