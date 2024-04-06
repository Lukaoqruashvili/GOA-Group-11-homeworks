def my_func(arr):
    join_str = "+"
    new_str = ""
    new_list = []
    for i in arr:
        new_str += join_str + str(i)
    return new_str[1:]

print(my_func([1,2,3,4]))