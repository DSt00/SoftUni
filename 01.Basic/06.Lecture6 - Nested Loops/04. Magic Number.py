starting_number = int(input())
ending_number = int(input())
magic_number = int(input())
result = 0
is_found = False
counter = 0

for i in range(starting_number, ending_number + 1):
    if not is_found:
        for j in range(starting_number, ending_number + 1):
            result = i + j
            counter += 1
            if result == magic_number:
                is_found = True
                print(f'Combination N:{counter} ({i} + {j} = {magic_number})')
                break
if not is_found:
  print(f'{counter} combinations - neither equals {magic_number}')

