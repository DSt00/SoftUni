budget = float(input())
season = input()
type_of_accommodation = ''


if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        price = budget * .3
    else:
        price = budget * .7
elif budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        price = budget * .4
    else:
        price = budget * .8
elif budget > 1000:
    place = 'Europe'
    price = budget * .9
if season == 'summer':
    type_of_accommodation = 'Camp'
if season == 'winter' or place == 'Europe':
    type_of_accommodation = 'Hotel'

print(f'Somewhere in {place}')
print(f'{type_of_accommodation} - {price:.2f}')
