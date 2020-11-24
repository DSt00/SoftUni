number_of_pours = int(input())
total = 0
for i in range(number_of_pours):
    liters = int(input())
    total += liters
    if total > 255:
        print('Insufficient capacity!')
        total -= liters
print(total)
