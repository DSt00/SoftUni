current_record = float(input())
distance = float(input())
seconds_per_meter = float(input())

delay = distance // 15 * 12.5
result = distance * seconds_per_meter + delay

if result < current_record:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(current_record - result):.2f} seconds slower.')
