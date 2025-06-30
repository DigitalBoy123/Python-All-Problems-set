num = [1,33,55,6,3,7,8,5,4,22,45,23,56,22,87,65]
for i in num[:]:
    if i % 2 !=0: # Keep in mind that range is always used for integers, not for anything!
        num.remove(i)
print(num)
        