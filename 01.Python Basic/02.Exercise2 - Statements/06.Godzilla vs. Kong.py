budget = float(input())
statists = int(input())
clothes_per_person = float(input())
clothes_total = statists * clothes_per_person
decor = budget * .1

if statists > 150:
    clothes_total *= .9

if decor + clothes_total > budget:
    print("Not enough money!")
    print(f'Wingard needs {abs(decor + clothes_total - budget):.2f} leva more.')

else:
    print('Action!')
    print(f'Wingard starts filming with {abs(decor + clothes_total - budget):.2f} leva left.')