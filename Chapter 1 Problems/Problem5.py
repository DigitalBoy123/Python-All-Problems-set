import datetime
def current_datetime():
    now = datetime.datetime.now()
    print(f"The current date is: {now:%Y-%m-%d}")  # No % in format string, but still needed inside {}
    print(f"The current time is: {now:%H:%M:%S}")
    return now
print(current_datetime())
# This is the first method for current date and time.


import datetime
def current_datetime():
    now = datetime.datetime.now()
    print("Current date is: {:%Y-%m-%d}".format(now))
    print("Current time is: {:%H-%M-%S}".format(now))
    return now
print(current_datetime())
# This is the second method for current date and time.