n = int(input())
list_even = []
list_odd = []
list_negative = []
list_positive = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)
    if num >= 0:
        list_positive.append(num)
    else:
        list_negative.append(num)
word = input()
if word == 'even':
    print(list_even)
elif word == 'odd':
    print(list_odd)
elif word == 'positive':
    print(list_positive)
elif word == 'negative':
    print(list_negative)
