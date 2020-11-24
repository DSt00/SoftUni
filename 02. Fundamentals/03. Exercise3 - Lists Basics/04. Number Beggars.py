numbers = input()
beggars = int(input())
numbers = list(numbers.split(", "))
a = 0
sum_per_beggar = []
result = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


for iteration in range(beggars):
    for index in range(0 + iteration, len(numbers), beggars):
        sum_per_beggar.append(numbers[index])
    result.append(sum(sum_per_beggar))
    sum_per_beggar.clear()

print(result)


