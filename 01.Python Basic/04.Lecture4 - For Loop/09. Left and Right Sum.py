n = int(input())
sum1 = 0
sum2 = 0

for i in range(1, n + 1):
    value = int(input())
    sum1 = sum1 + value

for i in range(1, n + 1):
    value = int(input())
    sum2 = sum2 + value

if sum1 == sum2:
    print(f'Yes, sum = {sum2}')
else:
    print(f'No, diff = {abs((sum1 - sum2))}')
