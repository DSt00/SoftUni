type_of_tickets = input()
r = int(input())
c = int(input())
price = 0
seats = r * c

if type_of_tickets == 'Premiere':
    price = 12
elif type_of_tickets == 'Normal':
    price = 7.5
elif type_of_tickets == 'Discount':
    price = 5

print(f'{seats * price:.2f}')
