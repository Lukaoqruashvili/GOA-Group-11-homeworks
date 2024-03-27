def a(input_list):
    return [string for string in input_list if string.startswith('a')]

strings_list = ["luka", "application", "team", "amsterdam", "awoken", "crystal"]
filtered_list = a(strings_list)
print("strings starting with a:", filtered_list)