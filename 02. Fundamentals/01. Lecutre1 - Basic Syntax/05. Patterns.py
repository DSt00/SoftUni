number = int(input())

for i in range(1, number + 1):
    print(f'*' * i)
for i in range(number - 1, 0, -1):
    print(f'*' * i)
