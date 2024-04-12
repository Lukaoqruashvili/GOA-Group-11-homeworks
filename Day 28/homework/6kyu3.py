def pyramid(n):
    result = []
    for i in range(1, n + 1):
        result.append([1] * i)
    return result
    
    