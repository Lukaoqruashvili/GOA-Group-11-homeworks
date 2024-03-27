correct_password = "Goa best"
incorrect_count = -1

while True:
    user_password = input("Enter the password: ")
    incorrect_count += 1

    if user_password == correct_password:
        print("Correct password! Access granted.")
        break
    else:
        print("Incorrect password. Please try again.")

print(f"Number of incorrect attempts: {incorrect_count}")
