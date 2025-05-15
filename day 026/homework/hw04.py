def moshoreba(lst):
    int_count = sum(1 for i in lst if type(i) == int)
    intiani = [i for i in lst if type(i) != int]
    
    
    

    if len(intiani) == 1 and int_count == len(lst) - 1:
        lst.remove(intiani[0])
    return lst


print(moshoreba([1, 2, "hello world", 3]))