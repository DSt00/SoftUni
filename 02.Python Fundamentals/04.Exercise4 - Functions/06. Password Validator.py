RANGE_NUMBERS = range(48, 58)
RANGE_LOWERCASE = range(97, 123)
RANGE_UPPERCASE = range(65, 91)


def pass_checker(password):
    is_valid = True
    valid = True
    sum_numbers = 0
    pass_as_list = []
    pass_as_list[:0] = password
    if 6 > len(password) < 10:  # check if length is ok
        is_valid = False
        print('Password must be between 6 and 10 characters')
    for i in range(len(pass_as_list)):  # check if only letters and digits
        if ord(pass_as_list[i]) in RANGE_NUMBERS:
            sum_numbers += 1
        elif ord(pass_as_list[i]) not in RANGE_NUMBERS and ord(pass_as_list[i]) not in RANGE_LOWERCASE and ord(pass_as_list[i]) not in RANGE_UPPERCASE:
            is_valid = False
            valid = False
    if not valid:
        print('Password must consist only of letters and digits')
    if sum_numbers < 2:  # check if less than 2 digits
        is_valid = False
        print('Password must have at least 2 digits')


    if is_valid:
        print('Password is valid')


password = input()
pass_checker(password)
