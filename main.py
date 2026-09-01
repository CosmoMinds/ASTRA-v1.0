import json
import os
from dotenv import load_dotenv
load_dotenv()
from tracking import track_satellites
print("=========================================")
print("         Astra v1.0")
print("         Satellite Detection System")
print("=========================================")

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == os.getenv("ASTRA_USERNAME") and password == os.getenv("ASTRA_PASSWORD"):
        print("Login Successful")
        return True
    else:
        print("Invalid Login credentials")
        return False
       
def load_satellites():
    with open("tracking_satellites.json", "r") as file:
        satellites = json.load(file)
    return satellites
def search_satellite(satellites, search_term):
    results = []
    for satellite in satellites:
        if search_term.lower() in satellite["name"].lower():
            results.append(satellite)
    return results
def mission_details(satellites):
    print()
    print("====================================================")
    print("                 ISRO Mission Details")
    print("====================================================")
    for index, satellite in enumerate(satellites, start = 1):
        print(f"{index}, {satellite['name']}")
    selection = input("Enter satellite number: ")
    if selection.isdigit():
        selection = int(selection)

        if 1 <= selection <= len(satellites):
            satellite = satellites[selection - 1]

            print()
            print("================================================")
            print("               Mission Information")
            print("================================================")
            print("Mission              :", satellite['mission'])
            print("Launch Date          :", satellite['launch_date'])
            print("Launch Vehicle       :", satellite['launch_vehicle'])
            print("Orbit                :", satellite['orbit'])
            print("Status               :", satellite['status'])

            print("================================================")

            input("Press Enter to return...")

        else:
            print("Invalid Satellite Number")
    else:
        print("Enter a Valid Number. ")    
def dashboard():
    while True:
        print()
        print("================================================")
        print("                 Astra Dashboard")
        print("================================================")

        print("1. Satellite Database")
        print("2. Real-time Tracking")
        print("3. Mission Details")
        print("4. Satellite Statistics")
        print("5. Settings")
        print("6. Logout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            satellites = load_satellites()

            while True:
                print()
                print("=====================================================")
                print("                     Satellite Database")
                print("=====================================================")
                print("1. View All Satellites")
                print("2. Search Satellites")
                print("0. Back to Dashboard")
                database_choice = input ("Enter your choice: ")
                if database_choice == "1":
                    print()
                    print("=================================================")
                    print("                        All Satellites")
                    print("=================================================")
                    for index, satellite in enumerate(satellites, start = 1):
                        print(f"{index}. {satellite['name']}")
                    selection = input("\n Enter Satellite number to view details: ")
                    if selection.isdigit():
                        selection = int(selection)
                        if 1 <= selection <= len(satellites):
                            satellite = satellites[selection - 1]
                            print()
                            print("=========================================")
                            print("                 Satellite Details")
                            print("=========================================")
                            print("Name                 :", satellite["name"])
                            print("NORAD ID             :", satellite["norad_id"])
                            print("Launch Date          :", satellite["launch_date"])
                            print("Launch Vehicle       :", satellite["launch_vehicle"])
                            print("Orbit                :", satellite["orbit"])
                            print("Mission              :", satellite["mission"])
                            print("Status               :", satellite["status"])
                            print("=========================================")
                            input("Press Enter to continue")
                        else:
                            print("Invalid Satellite Number.")
                    else:
                        print("Please enter a valid number.")
                elif database_choice == "2":
                    search_term = input("Enter Satellite Name: ")
                    results = search_satellite(satellites, search_term)

                    print()
                    print("=======================================================")
                    print("                   Search Results")
                    print("=======================================================")

                    if results:
                        for index, satellite in enumerate(results, start = 1):
                            print(f"{index}. {satellite['name']}")
                        selection = input("\nEnter Satellite number to view details: ")
                        if selection.isdigit():
                            selection = int(selection)
                            if 1 <= selection <= len(results):
                                satellite = results[selection - 1]
                                print()
                                print("==========================================")
                                print("             Satellite Details")
                                print("==========================================")

                                print("Name                 :", satellite["name"])
                                print("NORAD ID             :", satellite["norad_id"])
                                print("Launch Date          :", satellite["launch_date"])
                                print("Launch Vehicle       :", satellite["launch_vehicle"])
                                print("Orbit                :", satellite["orbit"])
                                print("Mission              :", satellite["mission"])
                                print("Status               :", satellite["status"])
                                print("=========================================")
                                input("Press Enter to continue")
                            else:
                                print("Invalid Satellite Number.")
                        else:
                            print("Please enter a valid number.")
                    else:
                        print("No satellite found.")
                        input("Press Enter to continue...")
                elif database_choice == "0":
                    break
                else:
                    print("Invalid Choice")

        elif choice == "2":
            track_satellites()

        elif choice == "3":
            print("Opening Mission Details...")
            satellites = load_satellites()
            mission_details(satellites)

        elif choice == "4":

            satellites = load_satellites()

            total_satellites = len(satellites)

            status_types = {}

            category_types = {}

            for satellite in satellites:
                status = satellite["status"]

                if status in status_types:
                    status_types[status] += 1

                else:
                    status_types[status] = 1

                category = satellite["category"]

                if category in category_types:
                    category_types[category] += 1
                else:
                    category_types[category] = 1

            print()
            print("=====================================================================")
            print("                         Satellite Satistics")
            print("=====================================================================")

            print("Total Satellites :", total_satellites)

            print()
            print("Satellite Status")
            print("---------------------------------------------------------------------")

            for status, count in status_types.items():
                print(f"{status: <25}: {count}")

            print()
            print("Satellite Categories")
            print("---------------------------------------------------------------------")

            for category, count in category_types.items():
                print(f"{category: <25}: {count}")

            print("=====================================================================")

            input("Press Enter to return to the Dashboard")

        elif choice == "5":
            while True:
                print()
                print("====================================================")
                print("                    ASTRA Settings")
                print("====================================================")
                print("1. System Information")
                print("2. Data Source Information")
                print("0. Back to Dashboard")

                settings_choice = input("Enter your choice: ")

                if settings_choice == "1":

                    print()
                    print("====================================================")
                    print("                 System Information")
                    print("====================================================")
                    print("Software Name    : Astra v1.0")
                    print("System Type      : Satellite Detection System")
                    print("Database         : satellites.json")
                    print("Tracking Engine  : Skyfield + SGP4")
                    print("====================================================")

                    input("Press Enter to continue...")

                elif settings_choice == "2":

                    print()
                    print("====================================================")
                    print("              Data Source Information")
                    print("====================================================")
                    print("Satellite Data   : Local JSON Database")
                    print("Tracking Data    : AMSAT")
                    print("Position Engine  : Skyfield / SGP4")
                    print("====================================================")

                    input("Press Enter to continue...")

                elif settings_choice == "0":
                    break

                else:
                    print("Invalid Choice. Please select 0-2.")

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