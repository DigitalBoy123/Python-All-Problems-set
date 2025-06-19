num = 89
if num<0:
    print("num is negative")
elif num>0:
    print("num is postive")
elif num==0:
    print("num is zero")
else:
    print("num not found")
    # This will check that num is not negative, positive, or zero.
# The last else statement is redundant and will never be executed until the above conditions are met.
# The code will always print "num is positive" since num is 89.
def check_num(num):
    if num < 0:
        return "num is negative"
    elif num > 0:
        return "num is positive"
    elif num == 0:
        return "num is zero"
    else:
        return "num not found"
    