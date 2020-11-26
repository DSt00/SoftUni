def merge_info():
    value = int(input())
    return value

result = {}
while True:
    command = input()
    if command == 'stop':
        break
    value = merge_info()
    if command in result:
        result[command] += value
    else:
        result[command] = value

for key in result:
    print(f'{key} -> {result[key]}')
