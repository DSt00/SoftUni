num_pages = int(input())
pages_per_hour = int(input())
num_days = int(input())

hours_per_book = num_pages / pages_per_hour
total_days = hours_per_book / num_days

print(total_days)
