legendary = {'fragments': 0, 'shards': 0, 'motes': 0}
junk = {}
while legendary['shards'] < 250 and legendary['fragments'] < 250 and legendary['motes'] < 250:
    materials = input().split()

    for i in range(0, len(materials), 2):
        key = materials[i + 1].lower()
        value = int(materials[i])

        if key in legendary:
            legendary[key] += value
        elif key in junk:
            junk[key] += value
        elif key not in junk:
            junk[key] = value
        if legendary['shards'] > 250 or legendary['fragments'] > 250 or legendary['motes'] > 250:
            break

if legendary['shards'] >= 250:
    print('Shadowmourne obtained!')
    legendary['shards'] -= 250
elif legendary['fragments'] >= 250:
    print('Valanyr obtained!')
    legendary['fragments'] -= 250
elif legendary['motes'] >= 250:
    print('Dragonwrath obtained!')
    legendary['motes'] -= 250

legendary = sorted(legendary.items(), key=lambda x: (-x[1], x[0]))
junk = sorted(junk.items(), key=lambda x: (x[0]))
legendary = {k: v for k, v in legendary}
junk = {k: v for k, v in junk}

for key, value in legendary.items():
    print(f'{key}: {value}')
for key, value in junk.items():
    print(f'{key}: {value}')
