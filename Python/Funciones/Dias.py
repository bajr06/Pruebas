def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    year = is_year_leap(year)

    if month >= 1 or month <= 12:
        if year == True:
            if month == 2:
                return 29
        elif year == False:
            if month == 2:
                return 28
    else:
        return None

    if month == 1:
            return 31
    elif month == 11:
            return 30
    else:
        return None




test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
