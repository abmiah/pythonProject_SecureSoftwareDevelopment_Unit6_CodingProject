"""The music_db.py is the main database file that holds the music artefacts data.
The file is used to create the database table structure, insert data into the table, fetch data from the table, and
display the data in a tabular format using the pandas module. The file also contains methods to add, edit, and delete
music artefacts in the database."""
"""The files uses a number of module libraries and classes to create a music database. 
These moduels inclues the sqlite3, datetime, hashlib, pandas, and time modules.
The classes used in the files are the Login class, AccountDB class, and MusicArtefactDB class.
The Login class is used to log in to the system using the username and password.
The AccountDB class is used to create the database connection and store the user's data.
The MusicArtefactDB class is used to create the database table structure, insert data into the table,
fetch data from the table, and display the data in a tabular format using the pandas module.
The class also contains methods to add, edit, and delete music artefacts in the database."""
import sqlite3
import datetime
import hashlib
import pandas as pd
import time
from login import Login


class MusicArtefactDB:
    """This section connects to the SQLite3 database"""
    def __init__(self):
        self.conn = sqlite3.connect("music_artefact.db")  # Connect to the SQLite3 database
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS music_artefact_db (
                            musicID integer PRIMARY KEY AUTOINCREMENT,
                            createdBy string, 
                            artistName string, 
                            publishDate string, 
                            lastModified string, 
                            musicTitle string,
                            musicLyrics string, 
                            musicScore string, 
                            musicRecordChecksum string, 
                            pathToFile string, 
                            isDeleted integer)""")

    @staticmethod
    def music_txt_file(music_file_path):
        """Use 'staticmethod()' method to only take a single parameter within the class.
        This function below 'def music_txt_file' enables the music lyric and music score file
        to be open as a 'read only' as highlighted as 'r'"""
        with open(music_file_path, 'r') as music_lyrics:
            for music_line in music_lyrics:
                return music_line.strip()

    @staticmethod
    def music_record_hash(file_path):
        """Use 'staticmethod()' method to only take a single parameter within the class.
        The function 'def music_record_hash' encrypts the file using the hashlib module sha256;
        the function has an assigned argument labelled 'file_path'"""
        file_hash = hashlib.sha256(file_path.encode()).hexdigest()
        return f"{file_hash}.mp3"

    def insert_data(self, data):
        """Use parameterised queries to prevent SQL injection"""
        self.cursor.executemany(
            "INSERT INTO music_artefact_db (createdBy, artistName, publishDate, lastModified, musicTitle, musicLyrics, musicScore, musicRecordChecksum, pathToFile, isDeleted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            data)
        self.conn.commit()

    def fetch_data(self):
        """This code is used to fetch the data from the table and used the standard SQL syntax """
        self.cursor.execute("SELECT * FROM music_artefact_db")

        return self.cursor.fetchall()

    def data_frame(self):
        """This is a DataFrame using the pandas module to display the data in a tabular format"""
        pd.options.display.max_columns = None
        pd.set_option("display.colheader_justify", "center")
        data_frame_var = pd.DataFrame(self.fetch_data(),
                                      columns=[
                                          'musicID', 'createdBy', 'artistName', 'publishDate', 'lastModified', 'musicTitle', 'musicLyrics', 'musicScore', 'musicRecordChecksum', 'pathToFile', 'isDeleted'
                                      ])
        return data_frame_var

    def add_music_artefacts(self, username):
        """This function is used to add music artefacts to the database"""
        user_login_name = Login()
        firstname, lastname = user_login_name.db.get_user_name(username)
        createdBy = user_login_name.fetch_login_data(firstname, lastname)

        artistName = str(input("Enter the artist name: "))

        """This section is used to create the date the music was created"""
        publish_date_input = input("Music publish date. Year, Month, Day: ")
        publish_date_input_split = publish_date_input.split(",")
        now = datetime.datetime.now()
        time_now = now.strftime("%H:%M:%S")
        year, month, day = map(int, publish_date_input_split)
        date_str = datetime.datetime(year, month, day).strftime("%Y-%m-%d")
        publishDate = f"{date_str} {time_now}"

        lastModified = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        musicTitle = str(input("Enter the title of the music: "))

        time.sleep(0.5)
        print("Song lyrics file has been uploaded:")
        musicLyrics = self.music_txt_file("song-file.txt")

        time.sleep(0.5)
        print("Music Score has been uploaded:")
        musicScore = self.music_txt_file("song-file-music-score.txt")

        time.sleep(0.5)
        print(f"'{musicTitle}.mp3' has been uploaded:")
        musicRecordChecksum = self.music_record_hash("song-file.txt")

        time.sleep(0.5)
        print(f"file path to '{musicTitle}.mp3': media/path/name/musicFile")
        pathToFile = "media/path/name/musicFile"
        isDeleted = 0

        date_to_insert = [(createdBy, artistName, publishDate, lastModified, musicTitle,
                          musicLyrics, musicScore, musicRecordChecksum, pathToFile, isDeleted)]

        self.insert_data(date_to_insert)

    def edit_music_artefacts(self, username, user):
        """This function is used to edit music artefacts in the database"""
        """Get the musicID of the entry to update"""
        musicID = input("Enter the musicID row number to update: ")

        try:
            """implemented the try and except block to catch any errors"""
            """Check if the user is authorised to edit the record"""
            self.cursor.execute("SELECT createdBy FROM music_artefact_db WHERE musicID = ?", (musicID,))
            result = self.cursor.fetchone()
            if result is None:
                print("No record found.")
                return 0
            createdBy = result[0]

            # Debugging lines delete once code is working
            print(f"DEBUG: username: {username}, createdBy: {createdBy}")
            print(f"DEBUG: user.isAdmin: {user.isAdmin}")

            if createdBy != username and not user.isAdmin:
                print("You are not authorised to edit this record.")
                return 0

            valid_columns = ["artistName", "publishDate", "musicTitle"]

            if user.isAdmin:
                column_to_update = input("Enter the column to update (artistName, publishDate, musicTitle): ")
            else:
                print("As a member, you can only update the musicTitle.")
                column_to_update = "musicTitle"

            if not user.isAdmin and column_to_update != "musicTitle":
                print("You are not authorised to update this column.")
                return 0

            if column_to_update not in valid_columns:
                print("Invalid column to update. Please enter a valid column to update.")
                return 0

            new_value = input(f"Enter the new value for {column_to_update}: ")

            if column_to_update == "publishDate":
                now = datetime.datetime.now()
                time_now = now.strftime("%H:%M:%S")

                date_format = ["-", ",", " ", ""]
                for formatting in date_format:
                    if formatting in new_value:
                        try:
                            year, month, day = map(int, new_value.split(formatting))
                            break
                        except ValueError:
                            continue
                else:
                    print("Invalid date format. Please enter a valid date format.")
                    print("Please enter date as year-month-day, year,month,day or year month day.")
                    return 0

                date_str = datetime.datetime(year, month, day).strftime("%Y-%m-%d")
                new_value = f"{date_str} {time_now}"

            """Update the entry in the database with the new value, // NOTE: potential SQL injection vulnerability // """
            update_sql = f"""
            UPDATE music_artefact_db 
            SET {column_to_update} = ? 
            WHERE musicID = ?"""

            self.cursor.execute(update_sql, (new_value, musicID))

            """Update the lastModified field in the database to the current date and time of the update"""
            lastModified = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            update_last_modified = """
            UPDATE music_artefact_db 
            SET lastModified = ? 
            WHERE musicID = ?
            """
            self.cursor.execute(update_last_modified, (lastModified, musicID))

            self.conn.commit()
            print("Record updated successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()  # Rollback changes in case of error
            return 0

    def delete_music_artefacts(self, user):
        """This function is used to delete music artefacts in the database"""
        if user.isAdmin:
            musicID = input("Enter the musicID row number to delete: ")
            delete_sql = """
            DELETE FROM music_artefact_db
            WHERE musicID = ?
            """
        else:
            print("You are not authorised to delete records.")
            return 0

        self.cursor.execute(delete_sql, (musicID,))
        self.conn.commit()

    def close_connection(self):
        """Last part of the code closes the connection"""
        self.conn.close()


"""The code below runs the class code of 'class MusicArtefactDB' and inserts data into the database table."""
"""The data is then fetched and printed to the console. The connection is then closed."""


if __name__ == "__main__":
    db = MusicArtefactDB()

    """Data to be inserted into the database table, these are preexisting music artefacts"""
    data_to_insert = [
        ('Papa Brown', 'James Brown', datetime.datetime(1965, 10, 1, 13, 30, 13).strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
         'I Got You (I Feel Good)', db.music_txt_file("i-feel-good.txt"),
         db.music_txt_file("i-feel-good_music-score.txt"), db.music_record_hash("i-feel-good.txt"),
         'media/path/name/musicFile', 0),

        ('Tania Turner', 'Tina Turner', datetime.datetime(1991, 10, 22, 11, 00, 55).strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'The Best',
         db.music_txt_file("the-best.txt"), db.music_txt_file("the-best_music-score.txt"),
         db.music_record_hash("the-best.txt"), 'media/path/name/musicFile', 0),

        ('Michael Fox', 'Michael Jackson', datetime.datetime(1982, 11, 30, 15, 30, 26).strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Billie Jean',
         db.music_txt_file("billie-jean.txt"), db.music_txt_file("billie-jean-music-score.txt"),
         db.music_record_hash("billie-jean.txt"), 'media/path/name/musicFile', 0),

        ('Whitney Jones', 'Whitney Houston', datetime.datetime(1992, 10, 22, 18, 25, 47).strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
         'I Will Always Love You',
         db.music_txt_file("i-will-always-love-you.txt"), db.music_txt_file("i-will-always-love-you-music-score.txt"),
         db.music_record_hash("i-will-always-love-you.txt"), 'media/path/name/musicFile', 0)

    ]

    db.insert_data(data_to_insert)
    df = db.data_frame()
    print(df.to_string())
    db.close_connection()
