num = int(input("Enter your number: "))
Stor_val = 1
for i in range(1,num+1):
    Stor_val *= i
print(f"The factorial is: {Stor_val}")