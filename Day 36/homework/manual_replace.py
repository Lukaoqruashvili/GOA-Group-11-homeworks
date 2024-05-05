def manual_replace(lst, old_value, new_value):
    for i in range(len(lst)):
        if lst[i] == old_value:
            lst[i] = new_value
    return lst
print(manual_replace([1,2,3,4,5], 3, 6))