academy = {}
num = int(input())

for _ in range(num):
    name = input()
    grade = float(input())
    if name in academy:
        academy[name].append(grade)
    else:
        academy[name] = []
        academy[name].append(grade)

new_academy = {}
for student, grades in academy.items():
    avrg = sum(grades) / len(grades)
    if avrg >= 4.5:
        new_academy[student] = sum(grades) / len(grades)

new_academy = sorted(new_academy.items(), key=lambda x: x[1], reverse=True)

for student, grades in new_academy:
    print(f'{student} -> {grades:.2f}')
