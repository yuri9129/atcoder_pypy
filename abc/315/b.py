m = int(input())
days_by_month = list(map(int, input().split()))

total_days = sum(days_by_month)
target_days = (total_days + 1) / 2

for month_num, days in enumerate(days_by_month):
    if days < target_days:
        target_days -= days
    else:
        print(f"{month_num + 1} {int(target_days)}")
        exit()



