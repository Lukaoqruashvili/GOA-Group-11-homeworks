def manual_count(list, count):
    counter = 0
    if count in list:
        for nums in list:
            if nums == count:
                counter += 1
    return counter

print(manual_count([1,2,3,4,5,5,5], 5))
