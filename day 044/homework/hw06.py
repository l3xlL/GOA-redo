def descending_order(num):
    s = str(num)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)