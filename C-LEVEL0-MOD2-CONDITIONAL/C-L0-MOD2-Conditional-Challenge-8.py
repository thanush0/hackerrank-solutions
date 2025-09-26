def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
def is_valid_date(x, y, z):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(z):
        days_in_month[1] = 29
    if 1 <= y <= 12 and 1 <= x <= days_in_month[y - 1]:
        return "Valid"
    return "Invalid"
x, y, z = map(int, input().split("/"))
if 1900 <= z <= 9999:
    print(is_valid_date(x, y, z))
else:
    print("Invalid")