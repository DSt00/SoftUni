from math import floor

in_hours = int(input())
in_minutes = int(input())

hours_in_minutes = in_hours * 60
total_minutes = hours_in_minutes + in_minutes + 15

hours = floor(total_minutes // 60)
minutes = total_minutes % 60

if hours > 23:
    hours -= 24

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')
