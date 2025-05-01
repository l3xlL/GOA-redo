# შეეცადეთ შექმნათ ფუნქცია, სადაც მომხმარებელი შეიყვანს რამე ორ არგუმენტს, მაგალითად "Goa" და Str,
# თქვენ უნდა შეამოწმოთ ემთხვევა თუ არა პირველი არგუმენტი მეორეს, ამ შემთხვევასი იქნება True რადგან "Goa" მართლაც არის String.

arg1 = input("arg 1: ")
arg2 = input("arg 2: ")

def check(arg1, arg2):


    if type(arg1) or type(arg2) == str:
        print(True)
    else:
        print(False)

check(arg1, arg2)