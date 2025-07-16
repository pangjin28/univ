def is_valid_date(m, d):
    days_in_month = [0, 31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    if 1 <= m <= 12 and 1 <= d <= days_in_month[m]:
        return "Yes"
    else:
        return "No"

m, d = map(int, input().split())
print(is_valid_date(m, d))
