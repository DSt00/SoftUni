income = float(input())
grade = float(input())
min_wage = float(input())
scholarship = 0

if grade >= 5.5:
    if income > min_wage:
        scholarship = int(grade * 25)
        print(f'You get a scholarship for excellent results {scholarship} BGN')
    else:
        if grade * 25 >= min_wage * 0.35:
            scholarship = int(grade * 25)
            print(f'You get a scholarship for excellent results {scholarship} BGN')
        else:
            scholarship = int(min_wage * .35)
            print(f'You get a Social scholarship {scholarship} BGN')
elif grade > 4.5 and income < min_wage:
    scholarship = int(min_wage * .35)
    print(f'You get a Social scholarship {scholarship} BGN')
else:
    print('You cannot get a scholarship!')
