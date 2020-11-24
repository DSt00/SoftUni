length = int(input())
width = int(input())
height = int(input())
percentage_taken = float(input())

volume = length * width * height
liters = volume * 0.001

output = liters * (1-percentage_taken*0.01)
print(output)