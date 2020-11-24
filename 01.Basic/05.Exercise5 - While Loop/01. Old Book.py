book_wanted = input()
current_book = input()
isFound = True
books_checked = 0
while current_book != book_wanted:
    if current_book == 'No More Books':
        isFound = False
        break
    books_checked += 1

    current_book = input()

if isFound:
    print(f'You checked {books_checked} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_checked} books.')
