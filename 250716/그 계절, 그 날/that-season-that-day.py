Y, M, D = map(int, input().split())

def is_valid_date(y,m, d):
    days_in_month = [0, 31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
        days_in_month[2] = 29
    
    if not (1 <= M <= 12 and 1 <= D <= days_in_month[M]):
        return -1

    if 3 <= m <= 5 and 1 <= d <= days_in_month[m]:
        return "Spring"
    elif 6 <= m <= 8 and 1 <= d <= days_in_month[m]:
        return "Summer"
    elif 9 <= m <= 11 and 1 <= d <= days_in_month[m]:
        return "Fall"
    else:
        return "Winter"

print(is_valid_date(Y, M, D))
