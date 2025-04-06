# შექმენით list-ი შემდეგი მნიშვნელობებით: [1,4,3,6,9,11,17,13,26,30], 
# თქვენი დავალებაა გამოტანოთ ლუწი რიცხვების ჯამი და კენტი რიცხვების რაოდენობა

numbers = [1,4,3,6,9,11,17,13,26,30]

even = sum(num for num in numbers if num % 2 == 0)
odd = len([num for num in numbers if num % 2 != 0])

print(even)
print(odd)