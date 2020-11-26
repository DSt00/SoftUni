basket = {}
while True:
    command = input()
    if command == "buy":
        break
    key, *value = command.split()
    price = float(value[0])
    quantity = int(value[1])

    if key in basket:
        basket[key].pop()
        basket[key].append(price)
        basket[key][0] += quantity
    else:
        basket[key] = []
        basket[key].append(quantity)
        basket[key].append(price)

for key, val in basket.items():
    val[0] = int(val[0])
    val[1] = float(val[1])
    print(f'{key} -> {val[0] * val[1]:.2f}')
