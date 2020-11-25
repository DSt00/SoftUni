flag = False
total = 0
while True:
    price = (input())
    if price == "special" or price == "regular":
        break

    flag = True
    price = float(price)
    if price < 0:
        print("Invalid price!")
    elif price == 0:
        print('Invalid order!')
    else:
        total += price


customer_type = price
after_taxes = total * 1.2
taxes = after_taxes - total
if customer_type == "special":
    after_taxes *= 0.9

if flag:
    print(f"Congratulations you've just bought a new computer!\n\
    Price without taxes: {total:.2f}$\n\
    Taxes: {taxes:.2f}$\n\
    -----------\n\
    Total price: {after_taxes:.2f}$")
else:
    print('Invalid order!')