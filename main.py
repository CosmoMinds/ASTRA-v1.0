import json

print("=========================================")
print("         Astra v1.0")
print("         Satellite Detection System")
print("=========================================")

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "Shriram" and password == "Astra@0324":
        print("Login Successful")
        return True
    else:
        print("Invalid Login credentials")
        return False
       
def load_satellites():
    with open("data/satellites.json", "r") as file:
        satellites = json.load(file)
    return satellites

def dashboard():
    while True:
        print()
        print("================================================")
        print("                 Astra Dashboard")
        print("================================================")

        print("1. Satellite Database")
        print("2. Real-time Tracking")
        print("3. ISRO Mission Details")
        print("4. Satellite Statistics")
        print("5. Settings")
        print("6. Logout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            satellites = load_satellites()

            print()
            print("=============================================")
            print("                     Satellite Database")
            print("=============================================")
            for index, satellite in enumerate(satellites, start = 1):
                print(f"{index}. {satellite['name']}")
            print("=============================================")
            selection = input("Enter the satellite number to view the details: ")
            if selection.isdigit():
                selection = int(selection)
                if 1 <= selection <= len(satellites):
                    satellite = satellites[selection - 1]
                    print()
                    print("=============================================")
                    print("                     Satellite Details")
                    print("=============================================")
                    print("Name     :", satellite["name"])
                    print("NORAD ID     :", satellite["norad_id"])
                    print("Launch Date      :", satellite["launch_date"])
                    print("Orbit        :", satellite["orbit"])
                    print("Mission      :", satellite["mission"])
                    print("Status       :", satellite["status"])
                    print("=============================================")
                    input ("Press Enter to return to the dashboard")
                else:
                    print("Invalid Satellite Number")
            else:
                print("Enter a Valid Number.")

        elif choice == "2":
            print("Opening Real-time Tracking...")

        elif choice == "3":
            print("Opening ISRO Mission Details...")

        elif choice == "4":
            print("Opening Satellite Statistics...")

        elif choice == "5":
            print("Opening Settings...")

        elif choice == "6":
            print("Logging out...")
            return "logout"

        elif choice == "7":
            print("Exiting Astra...")
            return "exit"

        else:
            print("Invalid Choice. Please select 1-7.")
while True:

    if login():

        result = dashboard()

        if result == "logout":
            print("Returning to login...")

        elif result == "exit":
            print("Astra shutting down.")
            break

    else:
        print("Try Again.")