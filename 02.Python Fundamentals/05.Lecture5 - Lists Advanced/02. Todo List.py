todo = [0 for _ in range(10)]
data = input()
while not data == "End":
    command = data.split('-')
    todo.insert(int(command[0]), command[1])
    data = input()
result = [task for task in todo if not task == 0]

print(result)
