n = int(input())
sum1 = 0
sum2 = 0
for i in range(1, n + 1):
    value = int(input())
    if i % 2 == 0:
        sum1 = sum1 + value
    else:
        sum2 = sum2 + value

if sum1 == sum2:
    print('Yes')
    print(f"Sum = {sum1}")
else:
    print('No')
    print(f'Diff = {abs(sum2 - sum1)}')
