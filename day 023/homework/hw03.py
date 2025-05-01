# შექმენით ფუნქცია სადაც მომხარებელი გასაცემს ასევე ორ არგუმენტს, თქვენი დავალებაა რომ უფრო დიდი რიცხვი გაყოთ უფრო პატარაზე (ასევე არ იცით რა მონაცმეთა ტიპია),
# თუ გამყოფი აღმოჩნდება 0 გამოიტანეთ ZeroDivissionError

def large_small (a, b):
    a = input("num1: ")
    b = input("num2: ")


    if a == 0 or b == 0:
        raise ZeroDivisionError("0ze ar gaiyofa")
    
    if a > b:
        return a / b
    else:
        return b / a
    
    
    
large_small()