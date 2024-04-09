def minimum(arr):
    maxvalue = arr[0]
    for num in arr:
        if num < maxvalue:
            maxvalue = num
    return maxvalue

def maximum(arr):
    maxvalue = arr[0]
    for num in arr:
        if num > maxvalue:
            maxvalue = num
    return maxvalue