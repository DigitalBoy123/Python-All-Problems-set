input = input("Enter your username: ")
length = len(input)
if length > 6 and "":
    print("The username you entered is too long!\n Try to enter the username in a specific range!")
else:
    print("OK! Your username verified!")