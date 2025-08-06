numbers = [1, 3, 5, 3, 7, 9, 1, 5, 11]

s = set()
dupes = set()

for num in numbers:
    if num in s:
        dupes.add(num)
    else:
        s.add(num)

print(dupes)