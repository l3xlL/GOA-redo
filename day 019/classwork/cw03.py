# 3) შექმენით ფუნქცია რომელიც იღებს მასივს და აბრუნებს ახალ მასივს კენტი ელემენტების გარეშე

lst = [1, 2, 3, 4, 5, 6, 7]

def remove_odds(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even

new = remove_odds(lst)
print(new)