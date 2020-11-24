def int_to_char(word):
    string = list(word)
    num_as_str = []

    while string[0].isdigit():
        num_as_str.append(string[0])
        string.pop(0)

    num = int(''.join(num_as_str))
    string.insert(0, chr(num))
    return ''.join(string)


def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


text = input().split()

for word in text:
    result = int_to_char(word)
    result = switch_letters(result)
    print(result, end=' ')
