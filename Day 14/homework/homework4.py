num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

startnum = min(num1, num2)
endnum = max(num1, num2)

for i in range(startnum, endnum + 1):
    if i % 5 == 0:
      print(i)