current_steps = 0
hasQuit = False
while current_steps < 10000:
    steps = input()
    if steps == "Going home":
        hasQuit = True
        continue
    steps = int(steps)
    current_steps += steps

    if hasQuit:
        break

difference = abs(current_steps - 10000)
if current_steps < 10000:
    print(f'{difference} more steps to reach goal.')
else:
    print("Goal reached! Good job!")
    print(f'{difference} steps over the goal!')

