rooms = int(input())
chairs = []
number_of_free_chairs = 0
flag = False

for room in range(rooms):
    chairs.append(input())
for el in range(len(chairs)):
    chairs[el] = chairs[el].split()

for el in range(len(chairs)):
    if chairs[el][0].count('X') >= int(chairs[el][1]):
        number_of_free_chairs += (chairs[el][0].count('X')) - int(chairs[el][1])
    else:
        print(f"{int(chairs[el][1]) - (chairs[el][0].count('X'))} more chairs needed in room {el + 1}")
        flag = True


if number_of_free_chairs > 0 and not flag:
    print(f'Game On, {number_of_free_chairs} free chairs left')
