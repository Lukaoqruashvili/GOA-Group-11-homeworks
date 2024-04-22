def variance(numbers): 
    n = len(numbers)
    average = sum(numbers) / n
    s = 0
    for i in numbers:
        s += i**2
    return (1/n * s) - (average ** 2)