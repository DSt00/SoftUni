queue = int(input())
lift = input().split()
lift = [int(_) for _ in lift]
lift_full = False
queue_end = False

i = 0
while i <= (len(lift)):
    lift_full = True if (sum(lift)) == len(lift) * 4 else False
    queue_end = True if queue == 0 else False
    if queue_end or lift_full:
        break
    if lift[i] == 4:
        i += 1
    else:
        lift[i] += 1
        queue -= 1

lift = [str(_) for _ in lift]
if queue_end:
    print('The lift has empty spots!')
if lift_full:
    print(f"There isn't enough space! {queue} people in a queue!")
print(" ".join(lift))
