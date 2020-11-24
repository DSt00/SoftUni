numbers = input().split()

numbers.sort(key=lambda x: str(x)[0])
numbers.reverse()
for i in numbers:
    print(i, end="")
