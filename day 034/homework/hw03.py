def dont_give_me_five(start, end):
    count = 0
    for number in range(start, end + 1):
        if '5' not in str(number):
            count += 1
            
    return count