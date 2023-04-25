# Account Creation
print("Account creation initiated..")
print()
print("Please enter your first name:")
first_name = str(input())
print()
print("Please enter your last name:")
last_name = str(input())
print()
print("Welcome " + first_name + " " + last_name + "!")
print()
print("Please enter an email address:")
user_email = str(input())
print()
print("Please enter a password:")
user_password = str(input())
print()
print("Account successfully created..")
print()

# Account Login Choice
print("Would you like to login?" + " Y/N")
print()
login = str(input())
if login == "Y":
    print()
    print("Login initiated..")
    print()
    # Account Login
    print("Please enter your email address:")
    login_email = str(input())
    if login_email == user_email:
        print()
        print("Please enter your password:")
        login_password = str(input())
        if login_password == user_password:
            print()
            print("Login successful")
        else:
            print()
            print("Password not recognized..")
            print()
            print("Login terminated..")
    else:
        print()
        print("Email not recognized..")
        print()
        print("Login terminated..")
elif login == "N":
    print()
    print("Login canceled..")
    print()
else:
    print("Login terminated..")
    print()
