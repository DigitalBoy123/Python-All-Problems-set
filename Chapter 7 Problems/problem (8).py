num = 0
if num < 2:
    print("Then num is not prime")
    exit()
for i in range(2,int(num**0.5) +1):
    if num % i ==0:
        print("Not prime!")
        break
else:
    print("Yes the number is Prime!")

 