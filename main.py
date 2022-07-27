def is_year_leap():
    year = int(input("Type year: "))
    if year % 4 == 0:
        return True
    else:
        return False

print("Year loop", is_year_leap())