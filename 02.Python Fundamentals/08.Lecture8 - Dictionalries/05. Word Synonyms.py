n = int(input())
result = {}

for _ in range(n):
    key = input()
    value = input()
    if key in result:
        result[key].append(value)
    else:
        result[key] = []
        result[key].append(value)

for key, value in result.items():
    print(f'{key} - {", ".join(value)}')
