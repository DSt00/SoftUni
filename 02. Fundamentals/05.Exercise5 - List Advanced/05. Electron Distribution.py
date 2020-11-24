number_of_electrons = int(input())
shells = []
max_possible = 0
shell_index = 1
while number_of_electrons > 0:
    max_possible = 2 * shell_index ** 2
    if max_possible > number_of_electrons:
        shells.append(number_of_electrons)
    else:
        shells.append(max_possible)
    number_of_electrons -= max_possible
    shell_index += 1

print(shells)