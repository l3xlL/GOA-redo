def info(name, surname, age, country):
    text = f"""full name: {name} {surname}. age: {age}, from: {country}."""
    return text

name = str(input("enter ur name: "))
surname = str(input("enter ur surname: "))
age = int(input("enter ur age: "))
country = str(input("enter ur country: "))

print(info(name, surname, age, country))