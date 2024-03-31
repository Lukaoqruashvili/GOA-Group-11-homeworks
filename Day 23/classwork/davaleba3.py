def findlasteven(numbers):
    for num in reversed(numbers):
        if num % 2 == 0:
            return num
nums = [1,2,3,4,5,6,7,8,9,11]
print(findlasteven(nums))