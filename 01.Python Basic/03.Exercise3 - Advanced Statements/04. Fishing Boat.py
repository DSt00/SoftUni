budget = int(input())
season = input()
number_of_fisherman = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if number_of_fisherman <= 6:
    price *= .9
elif 6 <= number_of_fisherman <= 11:
    price *= .85
elif number_of_fisherman >= 12:
    price *= .75

if (number_of_fisherman % 2) == 0 and season != 'Autumn':
    price *= .95

remain = abs(budget - price)

if budget >= price:
    print(f'Yes! You have {remain:.2f} leva left.')
else:
    print(f'Not enough money! You need {remain:.2f} leva.')
