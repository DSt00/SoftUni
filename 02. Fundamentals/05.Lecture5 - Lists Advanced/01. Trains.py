number_of_wagons = int(input())

train = number_of_wagons * [0]

command = input()

while not command == 'End':
    cmd = command.split()
    if cmd[0] == "add":
        train[-1] += int(cmd[1])
    elif cmd[0] == 'insert':
        train[int(cmd[1])] += int(cmd[2])
    elif cmd[0] == 'leave':
        train[int(cmd[1])] -= int(cmd[2])

    command = input()

print(train)
