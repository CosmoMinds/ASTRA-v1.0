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
            print("Opening Satellite Detection System...")

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