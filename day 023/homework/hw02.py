# შექმენით ფუნქცია სადაც მომხმარებელი გადასცემს ორ არგუმენტს, ორივე არის რიცხვი მაგრამ არ იცით თუ როგორი სახითაა იგი ჩაწერილი (string თუ integer), 
# თქვენი დავალებაა შეკრიბოთ ეს ორი რიცხვი, 
# მაგრამ გაითვალისწინოთ ისიც, რომ მომხმარებელმა შეიძლება შმეოიტანოს boolean ან float (String-ში ყოველთვის იქნება რიცხვები).


def add_numbers(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return f"jami aris: {num1 + num2}"

num1 = input("num1: ")
num2 = input("num2: ")

print(add_numbers(num1, num2))