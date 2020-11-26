d = {}
while True:
    command = input()
    if command == "End":
        break
    company, badge = command.split(" -> ")
    if company in d:
        if badge not in d[company]:
            d[company].append(badge)
    else:
        d[company] = []
        d[company].append(badge)

d = dict(sorted(d.items(), key=lambda x: x[0]))

for comp, val in d.items():
    print(f'{comp}')
    for bdge in val:
        print(f'-- {bdge}')

