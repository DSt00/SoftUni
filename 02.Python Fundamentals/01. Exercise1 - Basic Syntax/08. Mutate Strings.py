string_1 = input()
string_2 = input()
current_string = ''
prev_string = ''

for iteration in range(len(string_1)):
    for symbol in range(iteration + 1):
        current_string += string_2[symbol]
    for symbol2 in range(iteration + 1, len(string_1)):
        current_string += string_1[symbol2]
    if not current_string == prev_string:
        print(current_string)
    prev_string = current_string
    current_string = ''
