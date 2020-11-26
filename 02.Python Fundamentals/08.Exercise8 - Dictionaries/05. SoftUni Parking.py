registered = {}


def register(usr, li_n):
    if usr in registered:
        return f'ERROR: already registered with plate number {li_n}'
    else:
        registered[usr] = li_n
        return f'{usr} registered {li_n} successfully'


def unregister(usr):
    if usr in registered:
        registered.pop(usr)
        return f'{usr} unregistered successfully'
    else:
        return f'ERROR: user {usr} not found'


num = int(input())
for n in range(num):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        license_number = command[2]
        print(register(username, license_number))

    if command[0] == 'unregister':
        username = command[1]
        print(unregister(username))

for key, value in registered.items():
    print(f"{key} => {value}")
