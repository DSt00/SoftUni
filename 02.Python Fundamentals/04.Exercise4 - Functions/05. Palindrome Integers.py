def palindrome(list_numbers):
    for i in range(len(list_numbers)):
        list1 = []
        list2 = []
        list1[:0] = list_numbers[i]
        list2[:0] = list_numbers[i]
        list2.reverse()
        if list1 == list2:
            print('True')
        else:
            print('False')


text = input()
my_list = text.split(', ')
palindrome(my_list)
