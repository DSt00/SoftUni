import sys
number = input()
maximum = -sys.maxsize

while number != 'Stop':
    number = int(number)
    if number > maximum:
        maximum = number
    else:
        number = input()
print(maximum)

