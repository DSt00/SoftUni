age = int(input())
price_laundry = float(input())
price_toys = int(input())
number_of_toys = 0
money = 0
for i in range(1, age+1):
    if i % 2 != 0:
        number_of_toys = number_of_toys + 1
    else:
        money = money + i * 5
        money = money - 1

money = number_of_toys * price_toys + money

if money >= price_laundry:
    print(f'Yes! {abs(money - price_laundry):.2f}')
else:
    print(f'No! {abs(money - price_laundry):.2f}')
