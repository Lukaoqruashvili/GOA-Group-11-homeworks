def sum10(input_list):
    return sum(num for num in input_list if num > 10)

numberslist = [5, 10, 15, 20, 25]
print(sum10(numberslist))