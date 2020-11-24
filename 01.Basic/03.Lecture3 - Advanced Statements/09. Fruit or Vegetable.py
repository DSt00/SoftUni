# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".

word = input()

if word == 'banana' or word == 'apple' or word == 'kiwi' or word == 'cherry' or word == 'lemon' or word == 'grapes':
    print("fruit")
elif word == 'tomato' or word == 'cucumber' or word == 'pepper' or word == 'carrot':
    print('vegetable')
else:
    print("unknown")