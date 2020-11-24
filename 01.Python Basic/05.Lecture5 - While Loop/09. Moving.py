width = int(input())
length = int(input())
height = int(input())

count_free_space = width * length * height

command = input()  # брой пренесени кашони или текстът "Done"

while command != "Done":
    # брой пренесени кашони
    boxes = int(command)
    count_free_space -= boxes
    if count_free_space <= 0:
        print(f'No more free space! You need {abs(count_free_space)} Cubic meters more.')
        break
    command = input()
else:
    print(f'{count_free_space} Cubic meters left.')
