# 4) შექმენით ფუნქცია რომელიც იღებს მასივს ინტეჯერების და დააბრუნებს სტრინგ ამ ინტეჯერების გაერთიანების. მაგ ( [1,2,4,,18] --->  "12418"  )

numbers = [1, 2, 4, 18]

def join_numbers(numbers):
    result = ""
    for num in numbers:
        result += str(num)
    return result

joined_string = join_numbers(numbers)
print(joined_string)