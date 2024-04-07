def manual_min(lst):
    minvalue = lst[0]
    for num in lst:
        if num < minvalue:
            minvalue = num
    return minvalue   

print(manual_min([1,2,3,4,5]))     
        