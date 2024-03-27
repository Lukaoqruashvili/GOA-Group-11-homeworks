def filter_strings(input_list):
    return [string for string in input_list if len(string) > 5]

strings_list = ["apple", "banana", "orange", "pineapple", "kiwi", "watermelon"]
filtered_list = filter_strings(strings_list)
print("strings with length more than 5:", filtered_list)
