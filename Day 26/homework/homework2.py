def manual_max(lst):
    maxvalue = lst[0]
    for num in lst:
        if num > maxvalue:
            maxvalue = num
    return maxvalue

print(manual_max([1,2,3,4]))        
