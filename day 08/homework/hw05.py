import random

num1 = random.randint(1, 7)
num2 = num1 + random.randint(1, 5)
num3 = num2 + (num2 - num1)
num4 = num3 + (num2 - num1)
num5 = num4 + (num2 - num1)

tanmimdevroba = [num1, num2, num3, num4, num5]

hidden_index = random.randint(0, 4)
hidden_num = tanmimdevroba[hidden_index]
tanmimdevroba[hidden_index] = 0

print("gamoicani ricxvebis tanmimdevroba")
print(tanmimdevroba)

while True:
    user = int(input("sheiyvane ricxvi: "))

    if user == hidden_num:
        print("gamoicani!")
        break
    else:
        print("ar gamoicani")