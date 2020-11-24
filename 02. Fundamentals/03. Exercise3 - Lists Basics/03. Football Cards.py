input_string = input()
counterA = 0
counterB = 0
filtered_list = []
cards_given = list(input_string.split(" "))

for el in cards_given:
    if el not in filtered_list:
        filtered_list.append(el)

for index in range(len(filtered_list)):
    if 'A' in filtered_list[index]:
        counterA += 1
    if 'B' in filtered_list[index]:
        counterB += 1

team_a_remaining = 11 - counterA
team_b_remaining = 11 - counterB

print(f'Team A - {team_a_remaining}; Team B - {team_b_remaining}')
if team_a_remaining < 7 or team_b_remaining < 7:
    print('Game was terminated')
