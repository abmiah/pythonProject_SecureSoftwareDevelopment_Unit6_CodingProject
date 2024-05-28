# """Importing the AccountDB class from the account.py file, this file hold the database
# connection and users data"""
# """Importing the hashlib module to hash / encrypt the password using the sha256 algorithm"""
from account import AccountDB
import hashlib


class Login:
    """This is the main class used to log in to the system using the username and password.
    It also checks if the user is an admin and obtain the data from the AccountDB class."""
    def __init__(self):
        self.cursor = None
        self.firstname = None
        self.lastname = None
        self.isAdmin = None
        self.db = AccountDB()

    def login(self, username, password):
        """This function is used to log in to the system"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        print(f"Logging in with username: {username} and password: {password_hash}")

        users = self.db.fetch_data()
        if not users:
            print("No users found in the database.")
            return False

        for user in users:
            hashed_password = self.db.password_hash(password)
            if username == user[0] and hashed_password == user[5]:
                self.firstname = user[1]
                self.lastname = user[2]
                self.isAdmin = user[6]
                return f"{self.firstname}, {self.lastname}, {hashed_password}"
                if self.isAdmin:
                    return f"You are an admin."
                else:
                    return f"You are not an admin."
                return 0

        print("Invalid username or password.")
        return False

    def fetch_login_data(self, firstname, lastname):
        """This function is used to fetch the login data from the database"""
        try:
            self.db.cursor.execute("SELECT * FROM account_db WHERE firstname = ? AND lastname = ?", (firstname, lastname))
            user = self.db.cursor.fetchone()
            if user:
                user_name = f"{user[1]} {user[2]}"
                return user_name
            else:
                print("No user found.")
                return None
        except Exception as e:  # Catch any exceptions
            print(f"An error occurred: {e}")
            return None

    def close_connection(self):
        """This function is used to close the connection to the database"""
        self.db.close_connection()
