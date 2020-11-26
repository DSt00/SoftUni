bakery = {}
while True:
    command = input()
    if command == "statistics":
        break
    key, value = command.split(': ')
    value = int(value)
    if key in bakery:
        bakery[key] += value
    else:
        bakery[key] = value

print('Products in stock:')
for product in bakery:
    print(f'- {product}: {bakery[product]}')
print(f'Total Products: {len(bakery)}')
print(f'Total Quantity: {sum(bakery.values())}')

