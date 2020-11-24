from math import ceil
numbers = input().split(', ')
numbers = [int(num) for num in numbers]
groups = []
# number of groups
max_group_number = ceil(max(numbers) / 10)

for el in range(1, max_group_number + 1):
    groups.append([])
    groups[el-1] = [num for num in numbers if num <= el * 10]
    numbers = list(filter((lambda num: num > el * 10), numbers))

for i in range(len(groups)):
    print(f"Group of {i+1}0's: {groups[i]}")


