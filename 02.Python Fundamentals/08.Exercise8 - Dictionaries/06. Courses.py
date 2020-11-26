courses = {}

while True:
    command = input()
    if command == "end":
        break
    key, value = command.split(' : ')
    if key in courses:
        courses[key].append(value)
    else:
        courses[key] = [value]

courses = dict(sorted(courses.items(), key=lambda item: len(item[1]), reverse=True))
for k, v in courses.items():
    print(f'{k}: {len(courses[k])}')
    for name in sorted(v):
        print(f'-- {name}')
