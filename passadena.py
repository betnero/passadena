#!/bin/env python3

import secrets #Python 'secrets' module is more secure and fit for use with any security related application than the python'random' module
import string

#DISCLAIMER
print()
print("-" * 75)
print("DISCLAIMER: ")
print("A password to be considered relatively secure should be at least 12 to 15 characters long. It should include special characters, upper- and lowercase letters and digits.")
print("-" * 75)
print("ATTENTION!: ")
print("This password generator is not and should not be considered fully secure. It is to be treated with caution and as an assistive measure only.")
print("The user takes full responsibility of any direct or indirect damage inflicted by proper or inproper use of the software or its parts.")
print("-" * 75)
print()

# Looped to enable the user to run the script again or quit.
while True:
    
    # User input placed in a var
    usr = input("How long do you want the password to be? (MINIMUM 3) ")
    # Turn user input into an integer
    usr = int(usr)
    print()
    if usr < 3:
    	print("Try more than 2 characters...")
    	break

    # Definition of scope of numbers to be used for password generation
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Looped to generate a password with min. requirements of: at least 1 uppercase, 1 lowercasr and 1 digit
    while True:

        # Join all parts of the variable "alphabet" and itterate the number of times indicated by the user input
        password = "".join(secrets.choice(alphabet) for i in range(usr))

        # Check if the password meets minimum requirements
        if (any(i.islower() for i in password)
                and any(i.isupper() for i in password)
                and sum(i.isdigit() for i in password) >= 1):
            break

    # Print the result
    print(password)
    print()

    # Ask the user if another password will be generated or quit
    go_again = input("Want to generate another password?... (y/n)") 
    if go_again != "y":
        if go_again != "Y":
            break
