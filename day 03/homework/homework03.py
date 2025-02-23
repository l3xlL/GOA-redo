# task 1

# num1 = float(input("chawere pirveli ricxvi: "))
# num2 = float(input("chawere meore ricxvi: "))
# num3 = float(input("chawere mesame ricxvi: "))
# num4 = float(input("chawere meotxe ricxvi: "))

# jami = (num1 + num2 + num3 + num4) / 4

# print("am ricxvebis sashualo aritmetikuli aris: " + str(jami))

# # task 2

# saxeli = input("chawere sheni saxeli: ")
# gvari = input("chawere sheni gvari: ")

# print("mogesalmebit " + saxeli + " " + gvari)

# # task 3

# num5 = float(input("chawere pirveli ricxvi: "))
# num6 = float(input("chawere meore ricxvi: "))

# emoji = chr(128522)

# shedegi = str(num5) + emoji + str(num6)

# print("shedegi: " + shedegi)

import random

def magic_8_ball():
    
    answers = [
        "Yes",
        "No",
        "Maybe",
        "Definitely not",
        "Ask again later",
        "Cannot predict now",
        "Most likely",
        "Don't count on it"
    ]

    input("ask a question: ")

    answer = random.choice(answers)

    print("The Magic 8-Ball says:", answer)