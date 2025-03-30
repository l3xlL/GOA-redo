num = int(input("chawere ricxi 50-is chatvlit: "))

while num < 1 or num > 50:
    print("tavidan sheiyvane ricxi 50-is chatvlit")
    num = int(input("chawere ricxi 50-is chatvlit: "))

for i in range(num, 101, num):
    print(i)