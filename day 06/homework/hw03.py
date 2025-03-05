swori_pass = "random"
user_pass = input("chawere sheni paroli: ")

cda = 0

while user_pass != swori_pass and cda < 3:
    cda += 1
    print("paroli ar aris swori, scade tavidan.")
    user_pass = input("chawere sheni paroli: ")

if user_pass == swori_pass:
    print("paroli sworia")
else:
    print("paroli arasworia")