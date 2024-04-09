def friend(x):
    y = []
    for names in x:
        if len(names) == 4:
            y.append(names)
    return y
