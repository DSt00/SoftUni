n = int(input())
result = 0
counter = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):
            result = x1 + x2 + x3
            if result == n:
                counter += 1
print(counter)
