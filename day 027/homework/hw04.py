num1 = int(input("pirveli: "))
num2 = int(input("meore: "))
num3 = int(input("mesame: "))
num4 = int(input("meotxe: "))
num5 = int(input("mexute: "))

lst = []

lst.append(num1)
lst.append(num2)
lst.append(num3)
lst.append(num4)
lst.append(num5)

total = sum(lst)
print("the sum:", total)