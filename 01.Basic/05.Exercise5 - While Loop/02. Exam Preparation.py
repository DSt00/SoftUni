number_of_bad_grades = int(input())
bad_grades = 0
name_of_problem = input()
average_score = 0
number_of_problems = 0
last_problem = 0
flag = False

while name_of_problem != "Enough":
    grade = float(input())
    number_of_problems += 1
    if grade <= 4:
        bad_grades += 1
    average_score += grade
    last_problem = name_of_problem
    if bad_grades == number_of_bad_grades:
        flag = True
        break
    name_of_problem = input()

if flag:
    print(f'You need a break, {number_of_bad_grades} poor grades.')
else:
    print(f'Average score: {average_score/number_of_problems:.2f}')
    print(f"Number of problems: {number_of_problems}")
    print(f'Last problem: {last_problem}')

