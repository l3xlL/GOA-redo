def bevri(lst):
    types = [type(item) for item in lst]
    bevri = max(set(types), key=types.count)
    print("yvelaze xshirad meordeba: ", bevri)
    
    
sample = [1, "text", 2.5, 3, True, 4]
bevri(sample)