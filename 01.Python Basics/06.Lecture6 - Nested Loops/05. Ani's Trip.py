while True:
    destination = input()
    if destination == 'End':
        break
    budget = int(input())
    money_saved = 0
    while money_saved < budget:
        money_saved += int(input())
    print(f'Going to {destination}!')
