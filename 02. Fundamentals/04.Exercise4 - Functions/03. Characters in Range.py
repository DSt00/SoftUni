def characters_in_range_ascii(character_1, character_2):
    a = character_1
    b = character_2
    for i in range(ord(a) + 1, ord(b)):
        print(f'{chr(i)} ', end="")


character_1 = input()
character_2 = input()

characters_in_range_ascii(character_1, character_2)




