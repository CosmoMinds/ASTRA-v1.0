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
while True:
    if login():
        print("Opening Astra interface...")
        break
    else:
        print("Try Again.")
