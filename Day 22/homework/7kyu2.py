def descending_order(num):
    num_str = str(num)
    sorted_str = ''.join(sorted(num_str, reverse=True))
    return int(sorted_str)