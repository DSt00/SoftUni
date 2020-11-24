distance = float(input())
in_metric = input()
out_metric = input()
out = 0
if in_metric == 'mm':
    if out_metric == 'cm':
        out = distance / 10
    elif out_metric == 'm':
        out = distance / 1000
elif in_metric == 'cm':
    if out_metric == 'mm':
        out = distance * 10
    elif out_metric == 'm':
        out = distance / 100
elif in_metric == 'm':
    if out_metric == 'cm':
        out = distance * 100
    elif out_metric == 'mm':
        out = distance * 1000

print(f'{out:.3f}')
