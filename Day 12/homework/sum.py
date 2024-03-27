num = 1
even_sum = 0

while num <= 10:
    if num % 2 == 0:
        even_sum += num
    
    num += 1


print("sum of even numbers from 1 to 10 is", even_sum)
