user_input = input("chawere sityva: ")
reversed_string = ""

for i in user_input(len(user_input) - 1, -1, -1):

    reversed_string += user_input[i]

print("shemotrialebuli sityva:", reversed_string)