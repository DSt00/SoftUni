import sys
number = input()
minimum = sys.maxsize

while number != 'Stop':
    number = int(number)
    if number < minimum:
        minimum = number
    else:
        number = input()
print(minimum)

