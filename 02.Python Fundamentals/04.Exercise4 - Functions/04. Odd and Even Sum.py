def convert(string):
    list1 = []
    list1[:0] = string
    return list1


def odd_or_even_sum(number):
    sum_even = 0
    sum_odd = 0
    number = convert(number)
    for i in range(len(number)):
        number[i] = int(number[i])
        if number[i] % 2 == 0:
            sum_even += number[i]
        else:
            sum_odd += number[i]
    return sum_even, sum_odd


number = input()
sum_even, sum_odd = odd_or_even_sum(number)
print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')
