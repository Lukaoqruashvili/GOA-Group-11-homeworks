registered_pincode = 1234
authorized = False

while  authorized != True:
    user_input = int(input("please enter your pincode: "))

    if user_input == registered_pincode:
        print("Access Granted")
        authorized = True
    else:
        print("please try again")