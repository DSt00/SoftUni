days = int(input())
room = input()
grade = input()

nights = days - 1

if room == "room for one person":
    price = 18
elif room == "apartment":
    if days < 10:
        price = 25 * .7
    elif days <= 15:
        price = 25 * .65
    else:
        price = 25 * .5
else:
    if days < 10:
        price = 35 * .9
    elif days <= 15:
        price = 35 * .85
    else:
        price = 35 * .8

if grade == 'positive':
    price = price + .25 * price
else:
    price = price - .1 * price

print(f'{price * nights:.2f}')
