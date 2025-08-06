def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    total = 0
    i = n
    while i < m:
        total += i
        i += n

    return total