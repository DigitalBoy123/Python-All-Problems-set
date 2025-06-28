Inp = int(input("Enter your year: "))
def check_leap_year():
    if Inp % 4 == 0:
        return   f"Yes the year is leap: {Inp}"
    else:
        return f"No this is not a leap year: {Inp}"
print(check_leap_year())