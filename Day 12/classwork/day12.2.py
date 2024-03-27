num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

result = 0

for number in range(num1, num2 + 1):
    result = result + number
    print(number * number)
print(result)    
    