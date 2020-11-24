number_of_lines = int(input())
sum_of_ascii = 0
for i in range(number_of_lines):
    letters = input()
    sum_of_ascii += ord(letters)
print(f'The sum equals: {sum_of_ascii}')