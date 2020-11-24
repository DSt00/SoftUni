def total_price(product, quantity):
    result = None
    if product == 'coffee':
        result = quantity * 1.5
    elif product == 'water':
        result = quantity
    elif product == 'snacks':
        result = quantity * 2
    elif product == 'coke':
        result = quantity * 1.4
    return result


product = input()
quantity = int(input())

print(f'{total_price(product, quantity):.2f}')

