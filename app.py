import sys
from dbhelper import DBhelper


class Flipkart:

    def __init__(self):
        # Here we should connect to the database
        self.db = DBhelper()

        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        """)

        if user_input == '1':
            self.register()

        elif user_input == '2':
            self.login()

        else:
            sys.exit(1000)

    def register(self):

        pass


p = Flipkart()