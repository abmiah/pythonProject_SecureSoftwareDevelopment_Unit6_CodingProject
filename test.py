"""This file is used to test code snippets from the account.py, login.py, and script.py files."""

import hashlib
import datetime
import getpass
import datetime

########################

# def musicRecord(file_path):
#     file = hashlib.sha256(file_path.encode()).hexdigest()
#     print(f"{file}.mp3")
#
# musicRecord("password123")

########################
# def music_txt_file(music_file_path):
#     """This section locates the file and set to read mode 'r' which is stored in a variable 'music_lyrics'"""
#     with open(music_file_path, 'r') as music_lyrics:
#         for music_line in music_lyrics:
#             return music_line.strip()
#
#
# music_txt_file("i-feel-good.txt")

########################

# print(datetime.datetime(1991, 10, 10, 13, 20, 13))

########################

# # """This section connects to the SQLite3 database"""
# conn = sqlite3.connect(":memory:")
# cursor = conn.cursor()
#
# # """This section is used to create a table structure the syntax checks if this table does not exist"""
# cursor.execute("""CREATE TABLE IF NOT EXISTS account_db (
#                     username text,
#                     firstname text,
#                     lastname text,
#                     dateOfBirth integer,
#                     email text,
#                     isAdmin integer
#                     )""")
#
# # """Data to be inserted into the database table, these are existing  employees"""
# data_insert = [
#     ('james.brown', 'James', 'Brown', datetime.date(1933,5,3).isoformat(), 'james.brown@copyrightmusic.com', 0),
#     ('tina.turner', 'Tina', 'Turner', datetime.date(1939,11,26).isoformat(), 'tina.tuner@copyrightmusic.com', 1)
#     ]
#
# # """Use parameterised queries to insert data safely such as SQL injection"""
# cursor.executemany("INSERT INTO account_db VALUES (?, ?, ?, ?, ?, ?)", data_insert)
#
# # """Commit the changes to add to the database"""
# conn.commit()
#
# # """This code is used to fetch the data from the table and used the standard SQL sintax """
# cursor.execute("SELECT * FROM account_db")
# print(cursor.fetchall())
#
# # """Last part of the code closes the connection"""
# conn.close()

########################

# # """This function below 'def music_txt_file' enables the music lyric and music score file to be open as a 'read only' as highlighted as 'r'"""
# def music_txt_file(music_file_path):
#     """This section locates the file and set to read mode 'r' which is stored in a variable 'music_lyrics'"""
#     with open(music_file_path, 'r') as music_lyrics:
#         for music_line in music_lyrics:
#             return music_line.strip()
#
#
# # """The function 'def music_record_hash' encrypts the file using the hashlib module sha256; the function has an assigned argument labelled 'file_path'"""
# def music_record_hash(file_path):
#     """This section of the code first uses a variable name 'file' and then assigns it to 'hashlib.sha256()' module with the function assign argument"""
#     file_hash = hashlib.sha256(file_path.encode()).hexdigest()
#     return f"{file_hash}.mp3"
#
#
# # """Data to be inserted into the database table"""
# data = [
#     ('1', 'James Brown', datetime.datetime(1965, 10, 1, 13, 30, 13), datetime.datetime.now(), 'I Got You (I Feel Good)', music_txt_file("i-feel-good.txt"),
#      music_txt_file("i-feel-good_music-score.txt"), music_record_hash("i-feel-good.txt"), 'media/path/name/musicFile', 0),
#
#     ('2', 'Tina Turner', datetime.datetime(1991, 10, 22, 10, 10, 13), datetime.datetime.now(), 'The Best', music_txt_file("the-best.txt"),
#      music_txt_file("the-best_music-score.txt"), music_record_hash("the-best.txt"), 'media/path/name/musicFile', 0)
#     ]
#
# # """Use parameterised queries to insert data safely such as SQL injection"""
# cursor.executemany("INSERT INTO music_artefact_db VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
#
# # """Commit the changes to add to the database"""
# conn.commit()
#
# # """This code is used to fetch the data from the table and used the standard SQL sintax """
# cursor.execute("SELECT * FROM music_artefact_db")
# print(cursor.fetchone())
#
# # """Last part of the code closes the connection"""
# conn.close()

########################

# # """This section connects to the SQLite3 database"""
# conn = sqlite3.connect(":memory:")
# cursor = conn.cursor()
#
# # """This section is used to create a table structure the syntax checks if this table does not exist"""
# cursor.execute("""CREATE TABLE IF NOT EXISTS music_artefact_db (
#                     musicArtefactID integer,
#                     ownedBy string,
#                     createdData integer,
#                     lastModified integer,
#                     musicTitle string,
#                     musicLyrics string,
#                     musicScore string,
#                     musicRecordChecksum string,
#                     pathToFile string,
#                     isDeleted integer
#                     )""")
#
# # """This function below 'def music_txt_file' enables the music lyric and music score file to be open as a 'read only' as highlighted as 'r'"""
# def music_txt_file(music_file_path):
#     """This section locates the file and set to read mode 'r' which is stored in a variable 'music_lyrics'"""
#     with open(music_file_path, 'r') as music_lyrics:
#         for music_line in music_lyrics:
#             return music_line.strip()
#
#
# # """The function 'def music_record_hash' encrypts the file using the hashlib module sha256; the function has an assigned argument labelled 'file_path'"""
# def music_record_hash(file_path):
#     """This section of the code first uses a variable name 'file' and then assigns it to 'hashlib.sha256()' module with the function assign argument"""
#     file_hash = hashlib.sha256(file_path.encode()).hexdigest()
#     return f"{file_hash}.mp3"
#
#
# # """Data to be inserted into the database table"""
# data = [
#     ('1', 'James Brown', datetime.datetime(1965, 10, 1, 13, 30, 13), datetime.datetime.now(), 'I Got You (I Feel Good)', music_txt_file("i-feel-good.txt"),
#      music_txt_file("i-feel-good_music-score.txt"), music_record_hash("i-feel-good.txt"), 'media/path/name/musicFile', 0),
#
#     ('2', 'Tina Turner', datetime.datetime(1991, 10, 22, 10, 10, 13), datetime.datetime.now(), 'The Best', music_txt_file("the-best.txt"),
#      music_txt_file("the-best_music-score.txt"), music_record_hash("the-best.txt"), 'media/path/name/musicFile', 0)
#     ]
#
# # """Use parameterised queries to insert data safely such as SQL injection"""
# cursor.executemany("INSERT INTO music_artefact_db VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
#
# # """Commit the changes to add to the database"""
# conn.commit()
#
# # """This code is used to fetch the data from the table and used the standard SQL sintax """
# cursor.execute("SELECT * FROM music_artefact_db")
# print(cursor.fetchone())
#
# # """Last part of the code closes the connection"""
# conn.close()

########################

# time_now = datetime.datetime.now()
# time = time_now.time()
#
# it_date_tuple = 2024, 5, 2
#
# it_date = datetime.date(*it_date_tuple)
#
# date_and_time = datetime.datetime.combine(it_date, time)
# print(date_and_time)

# user_input = input("Enter the year and time following this format: -> yyyy,mm,dd,hh,mm: ")
# user_input_parts = user_input.split(",")
# year, month, day, hour, minutes = map(int, user_input_parts)
# datetime_str = datetime.datetime(year, month, day, hour, minutes)
# fortmatted_date = datetime_str.strftime("%Y-%m-%d %H:%M:%S")
# print(fortmatted_date)

# print(str(datetime_str))
# print(type(str(datetime_str)))
# print(str(datetime.datetime.now()))

# today_date = datetime.datetime(2024,5,5).strftime("%Y-%m-%d %H:%M:%S")
# print(today_date)
# print(type(today_date))

# user_input = input("Date Year, Month, Day: ")
# user_input_parts = user_input.split(",")
# now = datetime.datetime.now()
# time_now = now.strftime("%H:%M:%S")
# year, month, day = map(int, user_input_parts)
# date_str = datetime.datetime(year, month, day).strftime("%Y-%m-%d")
# print(date_str, time_now)

########################
"""Saved code"""
# def edit_music_artefacts(self, username, user):
#     """This function is used to edit music artefacts in the database"""
#     musicID = input("Enter the musicID row number to update: ")
#
#     """This section is used to check if the user is authorised to edit the record"""
#     self.cursor.execute("SELECT createdBy FROM music_artefact_db WHERE musicID = ?", (musicID,))
#     createdBy = self.cursor.fetchone()[0]
#     if createdBy != username:
#         print("You are not authorised to edit this record.")
#         return 0
#
#     valid_columns = ["artistName", "publishDate", "musicTitle"]
#     if user.isAdmin:
#         column_to_update = input("Enter the column to update (artistName, publishDate, musicTitle): ")
#     else:
#         print("Enter the column to update (artistName, publishDate, musicTitle): ")
#         column_to_update = input()
#
#     if column_to_update not in valid_columns:
#         print("Invalid column to update. Please enter a valid column to update.")
#         return 0
#
#     new_value = input(f"Enter the new value for {column_to_update}: ")
#
#     update_sql = f"""
#     UPDATE music_artefact_db
#     SET {column_to_update} = ?
#     WHERE musicID = ?
#     """
#     self.cursor.execute(update_sql, (new_value, musicID))
#
#     lastModified = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     update_last_modified = f"""
#     UPDATE music_artefact_db
#     SET lastModified = ?
#     WHERE musicID = ?
#     """
#
#     self.cursor.execute(update_last_modified, (lastModified, musicID))
#     self.conn.commit()

########################

# def edit_music_artefacts(self, username, user):
#     """This function is used to edit music artefacts in the database"""
#     musicID = input("Enter the musicID row number to update: ")
#
#     """This section is used to check if the user is authorised to edit the record"""
#     self.cursor.execute("SELECT createdBy FROM music_artefact_db WHERE musicID = ?", (musicID,))
#     createdBy = self.cursor.fetchone()[0]
#     if createdBy != username and not user.isAdmin:
#         print("You are not authorised to edit this record.")
#         return 0
#
#     valid_columns = ["artistName", "publishDate", "musicTitle"]
#     if user.isAdmin:
#         column_to_update = input("Enter the column to update (artistName, publishDate, musicTitle): ")
#     else:
#         print("Enter the column to update (musicTitle): ")
#         column_to_update = input()
#
#     if column_to_update not in valid_columns:
#         print("Invalid column to update. Please enter a valid column to update.")
#         return 0
#
#     new_value = input(f"Enter the new value for {column_to_update}: ")
#
#     update_sql = f"""
#     UPDATE music_artefact_db
#     SET {column_to_update} = ?
#     WHERE musicID = ?
#     """
#     self.cursor.execute(update_sql, (new_value, musicID))
