password = "GOAisthebest"

while True:
    input_password = input("Enter your password: ")

    if password == input_password:
        print("successfully logged in")
        break  
    else:
        print("incorrect password, try again ")
        try_again = input("try again? (yes or no): ")

        if try_again.lower() == "no":
            break  
        elif try_again.lower() != "yes":
            print("invalid input. Please enter 'yes' or 'no'")
