city = input()
volume = float(input())

if 0 <= volume <= 500:
    if city == "Sofia":
        print(f'{volume * .05:.2f}')
    elif city == "Varna":
        print(f'{volume * .045:.2f}')
    elif city == "Plovdiv":
        print(f'{volume * .055:.2f}')
    else:
        print("error")
elif 500 < volume <= 1000:
    if city == "Sofia":
        print(f'{volume * .07:.2f}')
    elif city == "Varna":
        print(f'{volume * .075:.2f}')
    elif city == "Plovdiv":
        print(f'{volume * .08:.2f}')
    else:
        print("error")
elif 1000 < volume <= 10000:
    if city == "Sofia":
        print(f'{volume * .08:.2f}')
    elif city == "Varna":
        print(f'{volume * .1:.2f}')
    elif city == "Plovdiv":
        print(f'{volume * .12:.2f}')
    else:
        print("error")
elif volume > 10000:
    if city == "Sofia":
        print(f'{volume * .12:.2f}')
    elif city == "Varna":
        print(f'{volume * .13:.2f}')
    elif city == "Plovdiv":
        print(f'{volume * .145:.2f}')
    else:
        print("error")
else:
    print("error")
