def already_had():
    return f"Place {position} already had Valentine's day."


def has_valentine():
    return f"Place {position} has Valentine's day."


houses = input().split('@')
houses = [int(_) for _ in houses]
position = 0
while True:
    command = input()
    if command == "Love!":
        break
    command = command.split()
    jump = int(command[1])

    if position + jump < len(houses):
        position = position + jump
        if houses[position] == 0:
            print(already_had())
        else:
            houses[position] -= 2
            if houses[position] == 0:
                print(has_valentine())
    else:
        position = 0
        if houses[position] == 0:
            print(already_had())
        else:
            houses[position] -= 2
            if houses[position] == 0:
                print(has_valentine())

fails = 0
for house in houses:
    if house:
        fails += 1

print(f"Cupid's last position was {position}.")
if fails == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {fails} places.')
