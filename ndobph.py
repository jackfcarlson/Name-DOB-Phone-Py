#a python program that prints the first name (up to 80 characters),
#DOB and phone #that the user has entered.

def ndobph():
    #get user information
    firstname = input("Enter your first name: ")

    lastname = input("Enter your last name: ")

    month = input("Enter the Numeric Month of Birth (July is '07'): ")

    day = input("Enter the day of your birth (ex. '14'): ")

    year = input("Enter the year of your birth(ex. '1999'): ")

    phone = input("Enter your phone number (10 digits): ")

    #print user information
    print("\n" * 2)
    print("Your Name is: " + firstname +" "+ lastname)
    print("Your birthdate is: "+ month + "-" + day + "-" + year)
    print("Your Phone number is: " + phone)
    print("\n" * 2)
