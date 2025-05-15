def type(value):
    if type(value) == str:
        print("literatura")
    elif type(value) == int or type(value) == float:
        print("matematika")
    elif type(value) == bool:
        print("qimia")
    else:
        print("error")