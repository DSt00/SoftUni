food = input().split()
stock = {}

for i in range(0, len(food), 2):
    key = food[i]
    value = int(food[i + 1])
    stock[key] = value

search = input().split()
for item in search:
    if item in stock:
        print(f'We have {stock[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")
