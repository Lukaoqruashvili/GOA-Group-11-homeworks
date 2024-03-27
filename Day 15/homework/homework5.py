user_input = int(input("enter a number: "))

if user_input < 2:
    print("not a prime number")
else:
    prime = True
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            prime = False
            break

    result = "prime" if prime else "not prime"
    print(f"{user_input} is {result}.")