number = int(input("enter start num: "))
number2 = int(input("enter end num: "))

def nums():
    for i in range(number, number2+1):
        if i % 2 == 0:
            print(i ** 2)
        else:
            print(i ** 0.5)


print(nums())