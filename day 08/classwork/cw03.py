user_input = input("sheiyvanet sam asoiani sityva: ")

for i in range(3):
    if len(user_input) != 3:
        print("unda chawerot 3 asoiani sityva.")
        user_input = input("sheiyvanet 3 asoiani sityva: ")

        print("Palindrome:", user_input[0] == user_input[2])
    else:
        break