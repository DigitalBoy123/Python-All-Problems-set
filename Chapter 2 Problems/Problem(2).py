Value_C = int(input("Enter your number in Celcius: "))
def C_to_F(Value_C):
    # return 9*Value_C/5 +32 
    return (Value_C * 1.8) + 32 # converts Celsius to Fahrenheit. Both formulas are valid, In one the fraction is used and in second the fraction is simplified.
y = C_to_F(Value_C)
print(f"{round(y,2)}°C") # Let's check that how this formula works and built for solving the problem. 
# In this forumula 1.8 or 9/5 came by dividing the difference between freezing and boiling point of water in Fahrenheit and Celsius 180/100.
# When we get such value then we mulitiply it with the value because we we know that 1 degree Celsius is equal to 1.8 degree Fahrenheit, so after multiplying it with the value we get the value in Fahrenheit.
#  But we also need to add the freezing point of water in Fahrenheit which is 32 degree. So we add 32 to the value to get the final value in Fahrenheit because 0 degree Celsius is equal to 32 degree Fahrenheit and we wanna start the calculation from 0 degree Celsius.
# So the final formula is (Value_C * 1.8) + 32. If you simplify the point then you will get the same formula as 9*Value_C/5 +32.
# The formula is derived from the fact that the freezing point of water is 0°C (32°F) and the boiling point is 100°C (212°F).

Value_F = int(input("Enter your number in Fahrenheit: "))
def F_to_C(Value_F):
    # return 5*(Value_F-32)/9
    return (Value_F - 32) / 1.8 # converts Fahrenheit to Celsius. Both formulas are valid, In one the fraction is used and in second the fraction is simplified.
y = F_to_C(Value_F)
print(f"{round(y,2)}°F") # We used the round function to round the value to 2 decimal places because the value can be in decimal and we want to show it in 2 decimal places.
# In this forumula 1.8 or 5/9 came by dividing the difference between freezing and boiling point of water in Fahrenheit and Celsius 180/100.If we wanna to convert the big value to small then we divide the 1.8 with the value because we we want to convert the value from Fahrenheit to Celsius.
# When we get such value then we mulitiply it with the value because we we know that 1 degree Fahrenheit is equal to 0.5555555555555556 degree Celsius, so after multiplying it with the value we get the value in Celsius.
