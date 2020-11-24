n = int(input())
word = input()
full_list = []
filtered_list = []
current_word = ''

for iterations in range(n):
    current_word = input()
    full_list.append(current_word)
    if word in current_word:
        filtered_list.append(current_word)
print(full_list)
print(filtered_list)
