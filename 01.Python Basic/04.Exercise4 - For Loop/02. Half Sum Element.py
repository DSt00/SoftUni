from sys import maxsize
number = int(input())
max_element = -maxsize
total_sum = 0
for i in range(1, number + 1):
    value = int(input())
    if value > max_element:
        max_element = value
    total_sum += value
total_sum = total_sum - max_element
if max_element == total_sum:
    print("Yes")
    print(f'Sum = {max_element}')
else:
    print("No")
    print(f'Diff = {abs(max_element - total_sum)}')
