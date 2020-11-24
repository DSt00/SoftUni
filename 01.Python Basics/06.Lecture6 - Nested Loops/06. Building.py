total_floors = int(input())
total_rooms = int(input())

for floor_number in range(total_floors, 0, -1):
    for room_number in range(total_rooms):
        if floor_number == total_floors:
            print(f'L{floor_number}{room_number} ', end='')
        elif floor_number % 2 == 0:
            print(f'O{floor_number}{room_number} ', end='')
        elif floor_number % 2 == 1:
            print(f'A{floor_number}{room_number} ', end='')
    print("")
