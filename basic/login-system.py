# First input
user_input = input("Enter data: ")
if user_input == "1":
    print("You entered:", user_input)

# User authentication
username = input("Enter username: ")
password = input("Enter password: ")

if (username == "admin" and password == "1234") or (username == "bg" and password == "1234"):
    print("Login successful")
else:
    print("Login failed")
