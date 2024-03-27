input = int(input("enter integer: "))

if input % 2 == 0:
    print("number is even")

elif input % 2 != 0:
    print("your number is not even, the next even number is " + str(input + 1 if (input + 1)% 2 == 0 else str(input + 2)))
else:
    print("invalid number, run this program again")