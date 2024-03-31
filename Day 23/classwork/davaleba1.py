def countevennums(numbers):
    count = 0
    
    for num in numbers:
        if num % 2 == 0:
            count += 1
    
    return count

numbers = [1, 2, 3, 4, 5, 8, 9, 12]
print(countevennums(numbers))