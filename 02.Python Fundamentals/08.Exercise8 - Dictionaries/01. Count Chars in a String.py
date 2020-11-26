text = input()
result = {}

for char in text:
    if char == " ":
        continue
    elif char in result:
        result[char] += 1
    elif char not in result:
        result[char] = 1

for key in result:
    print(f'{key} -> {result[key]}')
