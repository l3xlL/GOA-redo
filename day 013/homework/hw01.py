# მომხმარებელს შემოყავს სამნშნა რიცხვი. დათვალეთ და დაბეჭდეთ რა
# ნაშთს გვაძლევს შემოყვანილი რიცხვი მის ციფრთა ჯამზე გაყოფისას.
# მაგალითად, თუ მომხმარებელმა შემოიყვანა რიხვი 120, მისი ციფრთა
# ჯამია: 1 + 2 + 0 = 3. 120 ის ნაშთი 3 ზე გაყოფისას 0 ია. ამიტომ უნდა
# დაბეჭდოთ 0.



number = input("chawere samnishna ricxvi: ")

if len(number) == 3:
    asi = int(number[0])
    ati = int(number[1])
    erti = int(number[2])

    sumnum = asi + ati + erti
    sum = int(number) % sumnum

    print(sum)
else:
    print("unda chawero samnishna ricxvi")