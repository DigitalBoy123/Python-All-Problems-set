# numbers = []
# User_input = int(input("Enter your numbers: "))
# for item in User_input:
#     if 

a = int(input("Enter your number1: "))
b = int(input("Enter your number1: "))
choice = input("Enter your choice: ")
operations = {
    "ch1": "Division",
    "ch2": "Multiply",
    "ch3": "Sum",
    "ch4": "Subtract"
}
if operations[choice] == "Division":
    print(a/b)
elif operations[choice] == "Multiply":
    print(a*b)
elif operations[choice] =="Sum":
    print(a+b)
elif operations[choice] == "Subtract":
    print(a-b)
else:
    print("Invalid choice!")
