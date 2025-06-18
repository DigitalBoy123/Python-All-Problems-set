import calendar
from datetime import datetime
def get_calender():
    now = datetime.now()
    t = calendar.month(now.year, now.month)
    return t
print(get_calender())
   
import calendar
from datetime import datetime

def show_calendar():
    # Get current date
    today = datetime.now()
    current_year = today.year
    current_month = today.month
    
    # Show current month calendar
    print("THIS MONTH'S CALENDAR:")
    print(calendar.month(current_year, current_month))
    
    # Show next month calendar
    if current_month == 12:
        next_month = 1
        next_year = current_year 
        
    else:
        next_month = current_month + 2
        next_year = current_year
    
    print("\nNEXT MONTH'S CALENDAR:")
    print(calendar.month(next_year, next_month))
    
    # Show same month next year
    print("\nSAME MONTH NEXT YEAR:")
    print(calendar.month(current_year + 1, current_month))

# Run the program
show_calendar()