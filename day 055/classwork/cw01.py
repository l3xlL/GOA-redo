def stray(arr):
    for x in set(arr):
        if arr.count(x) == 1: return x