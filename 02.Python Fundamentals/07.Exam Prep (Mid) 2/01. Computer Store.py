
total = 0



while True:
    price = (input())
    if price == "special" or price == "regular":
        break

    price = float(price)
    if price < 0:
        print("Invalid order!")
    elif price == 0:
        print('Invalid order!')
    else:
        total += price

print(price)
#customer_type =