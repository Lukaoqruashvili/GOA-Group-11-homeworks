def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)