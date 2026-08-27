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
def search_satellite(satellites, search_term):
    results = []
    for satellite in satellites:
        if search_term.lower() in satellite["name"].lower():
            results.append(satellite)
    return results

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