# Дадено число е валидно, ако е в диапазона [100…200] или е 0.

number = int(input())

if (number < 100 or number > 200) and number != 0:
    print('invalid')
