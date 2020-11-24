numbers = list(map(lambda x: int(x), input().split(", ")))
indexes = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        indexes.append(i)

print(indexes)
