Use_inp = input("Enter your password: ")
len = len(Use_inp)
digits = "0123456789"
if len<=8 and any(d in Use_inp for d in digits):
    print("Yes! Your password meet criteria!")
else:
    print("No! Your password not meet criteria")
  
