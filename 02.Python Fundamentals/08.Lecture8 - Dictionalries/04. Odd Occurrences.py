words = input().split()
my_dict = {}
words = [w.lower() for w in words]

for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

result = []
for key in my_dict:
    if my_dict[key] % 2 == 1:
        result.append(key)

print(' '.join(result))
