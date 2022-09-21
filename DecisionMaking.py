## Decision Making with logic operators in Python

details = {
    "Sam" : "ABC",
    "John" : "XYZ",
    "Raj" : "PQR"
}

userName = input("Enter your name: ")

if userName in details:
    password = input("Enter your password: ")
    if password == details[userName]:
        print("Login Successful!")
    else:
        print("Check your Password!")
else:
    print("You are NOT in the system, Please Check your Username!")
