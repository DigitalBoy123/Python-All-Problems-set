num = int(input("Enter your number: "))  
for i in range(num):
    Spaces =" "* (num-i-1)
    Stars ="*"* (2*i+1)
    print(Spaces,Stars)