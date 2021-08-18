import calendar

m, d, y = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
