# """This script is used to create a database connection and insert data into the database table.
# The data is then fetched and printed to the console. The connection is then closed."""
# """The following modules are imported. SQLite3 is used to create a database connection and manage the database.
# The datetime module is used to store the date of birth of the employees.
# The hashlib module is used to hash the password using the sha256 algorithm."""
import sqlite3
import datetime
import hashlib


class AccountDB:
    """This section connects to the SQLite3 database using the connect method and creates a cursor object
    to execute SQL commands."""
    def __init__(self):
        self.user_password_hash = None
        self.conn = sqlite3.connect("account.db")
        self.cursor = self.conn.cursor()
        # """This section is used to create a table structure the syntax checks if this table does not exist"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS account_db (
                            username text,
                            firstname text,
                            lastname text,
                            dateOfBirth integer,
                            email text,
                            password text,
                            isAdmin integer
                            )""")

    def insert_data(self, data_insert):
        """Use parameterised queries to insert data safely such as SQL injection.
        The self.conn.commit() is used to add to the database."""
        self.cursor.executemany("INSERT INTO account_db VALUES (?, ?, ?, ?, ?, ?, ?)", data_insert)
        """Commit the changes to add to the database"""
        self.conn.commit()

    def password_hash(self, password):
        """This code is used to hash the password using the sha256 algorithm"""
        self.user_password_hash = hashlib.sha256(password.encode()).hexdigest()
        return self.user_password_hash

    def fetch_data(self):
        """This code is used to fetch the data from the table and uses the standard SQL syntax """
        self.cursor.execute("SELECT * FROM account_db")
        return self.cursor.fetchall()

    def get_user_name(self, username):
        """This code is used to fetch the user's first name and last name from the table based on the
        username."""
        self.cursor.execute('SELECT firstname, lastname FROM account_db WHERE username = ?', (username,))
        user = self.cursor.fetchone()
        if user:
            return user[0], user[1]
        else:
            return None, None

    def close_connection(self):
        """This code is used to close the connection to the database"""
        self.conn.close()


# """The code below runs the class code of 'class AccountDB' and inserts data into the database table.
# The data is then fetched and printed to the console. The connection is then closed."""

if __name__ == "__main__":
    db = AccountDB()

    """Data to be inserted into the database table, these are preexisting employees"""
    data_to_insert = [
        ('papa.brown', 'Papa', 'Brown', datetime.date(1933, 5, 3).isoformat(), 'papa.brown@copyrightmusic.com', db.password_hash("james@brown1933"), 0),
        ('tania.turner', 'Tania', 'Turner', datetime.date(1939, 11, 26).isoformat(), 'tania.tuner@copyrightmusic.com', db.password_hash("tina@turner1939"), 1),
        ('admin', 'Amrol', 'Miah', datetime.datetime.now(), 'test.test@copyrightmusic.com', db.password_hash("admin"), 1),
        ('user', 'Amrol2', 'Miah2', datetime.datetime.now(), 'test2.test2@copyrightmusic.com', db.password_hash("user"), 0)
    ]

    db.insert_data(data_to_insert)
    print(db.fetch_data())
    db.close_connection()
