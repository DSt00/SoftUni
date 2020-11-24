def convert(lst):
    return [-i for i in lst]


values = input()

li = list(values.split(" "))

for i in range(len(li)):
    li[i] = int(li[i])

print(convert(li))
