username = input()
password = input()
pass_check = input()

while pass_check != password:
    pass_check = input()
else:
    print(f'Welcome {username}!')
