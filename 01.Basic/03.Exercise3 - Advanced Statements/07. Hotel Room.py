month = input()
nights = int(input())
price_studio = 0
price_apartment = 0

if month == "May" or month == 'October':
    price_studio = 50
    price_apartment = 65
    if 7 < nights < 13:
        price_studio *= .95
    elif nights > 14:
        price_studio *= .7
elif month == 'June' or month == 'September':
    price_studio = 75.2
    price_apartment = 68.7
    if nights > 14:
        price_studio *= .8
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apartment = 77

if nights > 14:
    price_apartment *= .9

print(f'Apartment: {price_apartment * nights:.2f} lv.')
print(f'Studio: {price_studio * nights:.2f} lv.')
