def math_res():
    a = input("chawere matematikuri operacia: ")
    result = eval(a)

    if type(result) == int:
        print("type aris: int")
    elif type(result) == float:
        print("type airs: float")
    elif type(result) == bool:
        print("type aris: bool")
    else:
        print("type aris :", type(result))