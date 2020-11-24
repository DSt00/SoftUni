deposit = float(input())
term = int(input())
interest_rate_year = float(input())

interest_rate_month = deposit * interest_rate_year/100
total_sum = deposit + (term * interest_rate_month / 12)

print(total_sum)
