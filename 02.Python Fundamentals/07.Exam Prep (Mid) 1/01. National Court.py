from math import ceil

eff_1 = int(input())
eff_2 = int(input())
eff_3 = int(input())

total_ppl = int(input())

total_eff = eff_1 + eff_2 + eff_3
time = 0
while total_ppl > 0:
    time += 1
    total_ppl -= total_eff
    if time % 4 == 0:
        time += 1


print(f'Time needed: {time}h.')
