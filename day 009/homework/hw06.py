# შექმენით ფუნქცია რომელსაც გადაეცემა ორი პარამეტრი name, lastname. თქვენი დავალებაა გამოიტანოთ სახელის პირველი ასო, წერტილი და გვარი.

name = str(input("chawere saxeli: "))
lastname = str(input("chawere gvari: "))

def say_name(name, lastname):
    return f"{name[0]}. {lastname}"

result = say_name(name, lastname)
print(result)