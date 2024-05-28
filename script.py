# """The script.py file is the main file that runs the program. It is used to interact with the user and
# call the methods from the other classes. The script.py file imports the Login class from the login.py file
# and the MusicArtefactDB class from the music_db.py file. The script.py file contains the main code
# that interacts with the user, such as logging in, displaying options, and calling the appropriate
# methods based on the user's input."""
"""The script file uses similar modules and classes as the account.py and login.py files.
The script file interacts with the user by displaying options and calling the appropriate methods
based on the user's input. The script file imports the Login class from the login.py file and the
MusicArtefactDB class from the music_db.py file. The script file contains the main code that interacts
with the user, such as logging in, displaying options, and calling the appropriate methods based on
the user's input."""
import getpass
import time
from login import Login
from music_db import MusicArtefactDB


if __name__ == "__main__":
    """This is the main function that runs the program. It interacts with the user by displaying options 
    and calling the appropriate methods based on the user's input. The script.py file imports the Login 
    class from the login.py file and the MusicArtefactDB class from the music_db.py file. The script.py 
    file contains the main code that interacts with the user, such as logging in, displaying options, 
    and calling the appropriate methods based on the user's input."""
    while True:
        print("Welcome to the Music Copyright Database! Please login.")
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        user = Login()
        if user.login(username, password):
            user_type = "Admin" if user.isAdmin else "Member"
            print(f"You are now logged in. "
                  f"Welcome {user.firstname} {user.lastname}! "
                  f"Your account type: {user_type}")
            print("---" * 20)
            break

        print("Username and password do not match. Please try again.")

    while True:
        """This block of code is used to display the options to the user"""
        time.sleep(0.5)

        print(f"{user.firstname} select an option:")
        print("1. View music artefacts")
        print("2. Add music artefacts")
        print("3. Update music artefacts")
        print("4. Delete music artefacts")
        print("5. Logout")

        time.sleep(0.5)
        print("---" * 20)
        time.sleep(1)

        user_option = input("Enter your option: ")
        if user_option == "1":
            print("View music artefacts")
            music_data_records = MusicArtefactDB()
            print(music_data_records.data_frame().to_string())
            print("---" * 20)
            continue

        elif user_option == "2":
            print("Add music artefacts")
            music_data_records = MusicArtefactDB()
            music_data_records.add_music_artefacts(username)
            print(music_data_records.data_frame().to_string())
            print("---" * 20)
            continue

        elif user_option == "3":
            print("Update music artefacts")
            print("---" * 20)
            print("Current music artefacts")
            music_data_records = MusicArtefactDB()

            music_data_records.edit_music_artefacts(username, user)
            print(music_data_records.data_frame().to_string())
            print("---" * 20)
            continue

        elif user_option == "4":
            print("Delete music artefacts")
            music_data_records = MusicArtefactDB()
            music_data_records.delete_music_artefacts(user)
            print(music_data_records.data_frame().to_string())
            print("---" * 20)
            continue

        elif user_option == "5":
            print("Logging out...")
            user.close_connection()
            break
        else:
            print("Invalid option. Please try again.")
            continue
        break

    music_data_records.close_connection()
