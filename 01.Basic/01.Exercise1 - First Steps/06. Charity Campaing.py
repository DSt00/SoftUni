num_days = int(input())
num_cooks = int(input())
num_cakes = int(input())
num_waffles = int(input())
num_pancakes = int(input())

cakes = num_cakes * num_cooks * num_days
waffles = num_waffles * num_cooks * num_days
pancakes = num_pancakes * num_cooks * num_days

sum_cakes = cakes * 45
sum_waffles = waffles * 5.8
sum_pancakes = pancakes * 3.2

total_sum = sum_cakes + sum_waffles + sum_pancakes

charity_sum = total_sum - total_sum / 8
print(charity_sum)
