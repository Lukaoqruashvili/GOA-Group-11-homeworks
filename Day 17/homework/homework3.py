def filter_even_numbers(inputlist):
    return [num for num in inputlist if num % 2 == 0]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(numbers_list)
print(filtered_list)