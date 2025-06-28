t = 345
if t % 5==0 and t % 3==0:
    print("Yes! the number is multiple of 3 and 5")
else:
    print("No! the number is not the multiple of 3 and 5")



# This is just for checking the multiples are present in number or not. It is not a part of this program.
y = 345
factors = []
for i in range(1,y+1):
    if y % i == 0:
        factors.append(i)
print(factors)

