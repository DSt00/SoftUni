def perfect_number(number):
    sum_divisors = 0
    is_perfect = False
    for integers in range(1, number):
        if number % integers == 0:
            sum_divisors += integers
    if sum_divisors == number:
        is_perfect = True
    return is_perfect


number = int(input())
result = perfect_number(number)

if result:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
