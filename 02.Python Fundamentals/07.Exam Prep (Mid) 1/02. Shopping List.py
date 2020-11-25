def urgent(item):
    flag = False
    for i in groceries:
        if i == item:
            flag = True
            continue
    if not flag:
        groceries.insert(0, item)

    return groceries


def unnecessary(item):
    flag = False
    for i in groceries:
        if i == item:
            flag = True
            continue
    if flag:
        groceries.remove(item)

    return groceries


def correct(old_item, new_item):
    flag = False
    index = None
    for i in groceries:
        if i == old_item:
            flag = True
            index = groceries.index(old_item)
            continue
    if flag:
        groceries.pop(index)
        groceries.insert(index, new_item)

    return groceries


def rearrange(item):
    flag = False
    for i in groceries:
        if i == item:
            flag = True
            continue
    if flag:
        groceries.insert(len(groceries), item)
        groceries.remove(item)

    return groceries


groceries = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split()
    if command[0] == "Urgent":
        groceries = urgent(command[1])
    elif command[0] == 'Unnecessary':
        groceries = unnecessary(command[1])
    elif command[0] == 'Correct':
        groceries = correct(command[1], command[2])
    elif command[0] == 'Rearrange':
        groceries = rearrange(command[1])

print(', '.join(groceries))
