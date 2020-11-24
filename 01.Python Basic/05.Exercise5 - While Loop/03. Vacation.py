needed_money = float(input())
money_on_hand = float(input())
days_passed = 0
counter = 0
hasFailed = False

while money_on_hand < needed_money:
    command = input()
    amount = float(input())
    days_passed += 1
    if command == 'save':
        money_on_hand += amount
        counter = 0
    elif command == 'spend':
        money_on_hand -= amount
        if money_on_hand < 0:
            money_on_hand = 0
        counter += 1
    if counter == 5:
        hasFailed = True
        break

if hasFailed:
    print("You can't save the money.")
    print(days_passed)
else:
    print(f'You saved the money for {days_passed} days.')
