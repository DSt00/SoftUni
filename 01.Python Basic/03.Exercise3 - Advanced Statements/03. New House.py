# Roses Dahlias Tulips, Narcissus или Gladiolus

type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
price_per_flower = 0
total_sum = 0

if type_of_flowers == 'Roses':
    price_per_flower = 5
    total_sum = number_of_flowers * price_per_flower
    if number_of_flowers > 80:
        total_sum *= .9
elif type_of_flowers == 'Dahlias':
    price_per_flower = 3.8
    total_sum = (number_of_flowers * price_per_flower)
    if number_of_flowers > 90:
        total_sum *= .85
elif type_of_flowers == 'Tulips':
    price_per_flower = 2.8
    total_sum = (number_of_flowers * price_per_flower)
    if number_of_flowers > 80:
        total_sum *= .85
elif type_of_flowers == 'Narcissus':
    price_per_flower = 3
    total_sum = number_of_flowers * price_per_flower
    if number_of_flowers < 120:
        total_sum *= 1.15
elif type_of_flowers == 'Gladiolus':
    price_per_flower = 2.5
    total_sum = (number_of_flowers * price_per_flower)
    if number_of_flowers < 80:
        total_sum *= 1.2

remain = abs(budget - total_sum)
if budget >= total_sum:
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {remain:.2f} leva left.')
elif total_sum > budget:
    print(f'Not enough money, you need {remain:.2f} leva more.')
