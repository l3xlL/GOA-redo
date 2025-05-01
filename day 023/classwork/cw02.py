# codewars

def count_positives_sum_negatives(arr):
    
    if arr == []:
        return[]
        
    
    pos = 0
    neg = 0
    
    for num in arr:
        if num > 0:
            pos = pos + 1
        elif num < 0:
            neg = neg + num
            
    return[pos,neg]