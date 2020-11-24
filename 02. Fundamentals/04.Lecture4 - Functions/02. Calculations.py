def calculate(op, num_1, num_2):
    result = None
    if op == 'multiply':
        result = num_1 * num_2
    elif op == 'divide':
        result = num_1 // num_2
    elif op == 'add':
        result = num_1 + num_2
    elif op == 'subtract':
        result = num_1 - num_2
    return result


operator = input()
number_1 = int(input())
number_2 = int(input())


print(calculate(operator, number_1, number_2))