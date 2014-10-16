#Jarod Pierre Murton
#Development exercise iteration
#16/10/14

total = 0
number = int(input("Please enter a number: "))
number_2 = number - 1

for count in range(number):
    total = number * number_2
    number = number - 1
    number_2 = number_2 - 1
    if number > 0:
            print(total)
