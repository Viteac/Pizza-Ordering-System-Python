import os

pay = []
ordered = []
total_Day = 0

lop = ''' _____ _                 ____          _              _____           _                 
 |  __ (_)               / __ \        | |            / ____|         | |                
 | |__) | __________ _  | |  | |_ __ __| | ___ _ __  | (___  _   _ ___| |_ ___ _ __ ___  
 |  ___/ |_  /_  / _` | | |  | | '__/ _` |/ _ \ '__|  \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |   | |/ / / / (_| | | |__| | | | (_| |  __/ |     ____) | |_| \__ \ ||  __/ | | | | |
 |_|   |_/___/___\__,_|  \____/|_|  \__,_|\___|_|    |_____/ \__, |___/\__\___|_| |_| |_|
                                                              __/ |                      
                                                             |___/                       '''


print('Welcome to Pizza House')

print('Choose Your Pizza\nS. Small pizza $15.\nM. Medium Pizza: $20.\nL.Large Pizza $25\nQ - quit')


def topping(n):
    if n == 's':
        pizz_price = 15
        size_pi = 'Small Pizza:$15'
        pepperoni_price = 2
    elif n == 'm':
        pizz_price = 20
        size_pi = 'Medium Pizza:$20'
        pepperoni_price = 3
    else:
        pizz_price = 25
        size_pi = 'large Pizza:$25'
        pepperoni_price = 4
        
    this_sum = []
    tops = []
    tops.append(size_pi)
    this_sum.append(pizz_price)
    while True:
        os.system('clear')
        print(lop)
        print(f'Your Toppings: {tops}\nThis order: ${sum(this_sum)}')
        print(
            f'*Pepperoni - $ {str(pepperoni_price)} \n*Cheese - $1')
        toppings = input(f'Enter:\n"P"  - to ADD Pepperoni\n"C" - to ADD Cheese\n"d" - to DELETE order\n"Q" - to FINISH Pizza\n>>').lower()
        if toppings in 'pcdq':
            if toppings == 'p':
                this_sum.append(pepperoni_price)
                tops.append(f'Pepperoni:{pepperoni_price}')
            elif toppings == 'c':

                this_sum.append(1)
                tops.append('Cheese:$1')
            elif toppings == 'd':
                this_sum.clear()
                tops.clear()
            else:
                pay.extend(this_sum)
                ordered.extend(tops)
                break


def small():
    os.system('clear')
    this_sum = []
    tops = []
    print('* Pepperoni for small pizza +$2\n*Extra Cheese +$1')
    tops.append('Small Pizza:15')
    this_sum.append(15)
    while True:
        print(f'Your Toppings:{tops}\nThis order: ${sum(this_sum)}')
        toppings = input('Enter:\nP - to add Pepperoni\nC - to add Cheese\nQ to finish Pizza\n>>').lower()
        if toppings in 'pcq':
            if toppings == 'p':
                print('Pepperoni - "$2')
                this_sum.append(2)
                tops.append('Pepperoni:$2')
            elif toppings == 'c':
                print('Cheese -  $1')
                this_sum.append(1)
                tops.append('Cheese:$1')
            else:
                pay.extend(this_sum)
                ordered.extend(tops)
                break


def finito(n, t):
    os.system('clear')
    print(lop)
    print('Ordered:')
    for k in ordered:
        print(f'*{k}')
    print('_' * 20)
    bal = sum(pay)
    print(f'Total to pay: {bal}')
    while True:
        ispaid = input('\nPaid? Y/N').lower()
        if ispaid in 'yn':
            if ispaid == 'y':
                t += bal
                pay.clear()
                ordered.clear()
                return t


print('Welcome to Pizza House')

print('Choose Your Pizza\nS. Small pizza $15.\nM. Medium Pizza: $20.\nL.Large Pizza $25\nQ - quit')

while True:
    os.system('clear')
    print(lop)
    print(f'Orders: {ordered}')
    print(f'Total to Pay: ${sum(pay)}')
    print(f'Total today: ${total_Day}')
    print("-" * 30)
    pizza_choice = input('Choose the size\n Enter:  "S" - Small Pizza. "M" - Medium Pizza.  "L" - Large Pizza . "F" - Finish order & Pay\n>>').lower()
    if pizza_choice in 'smlf':
        if pizza_choice in 'sml':
            topping(pizza_coice)
        else:
            total_Day = finito(pay, total_Day)
