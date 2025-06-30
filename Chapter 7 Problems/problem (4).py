num = int(input("Enter your number of terms: "))
a,b = 0,1
for i in range(num):
    print(a,end="")
    a,b = b,a+b
