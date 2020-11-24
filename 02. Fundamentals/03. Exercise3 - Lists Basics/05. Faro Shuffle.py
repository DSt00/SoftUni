string = input()
shuffles = int(input())
deck = list(string.split())

top_card = deck[0]
bottom_card = deck[-1]
deck.pop(0)
deck.pop(-1)
half_split = len(deck) // 2
shuffled_deck = []

for iteration in range(shuffles):
    left_half = deck[:half_split]
    right_half = deck[half_split:len(deck)]
    for shuffle in range(half_split):
        shuffled_deck.append(right_half[shuffle])
        shuffled_deck.append(left_half[shuffle])
    deck = shuffled_deck.copy()
    shuffled_deck.clear()
deck.insert(0, top_card)
deck.append(bottom_card)

print(deck)
