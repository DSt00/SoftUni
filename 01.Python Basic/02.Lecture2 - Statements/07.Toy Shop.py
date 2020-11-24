price_excursion = float(input())
num_puzzle = int(input())
num_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_truck = int(input())

total_price = num_puzzle * 2.6 + num_dolls * 3 + num_teddy_bears * 4.1 + num_minions * 8.2 + num_truck * 2
num_toys = num_puzzle + num_dolls + num_teddy_bears + num_minions + num_truck

if num_toys >= 50:
    total_price = total_price * 0.75

rent = total_price * 0.1
total_price = total_price - rent

if total_price >= price_excursion:
    print(f'Yes! {total_price - price_excursion:.2f} lv left.')
else:
    print(f'Not enough money! {price_excursion - total_price:.2f} lv needed.')
