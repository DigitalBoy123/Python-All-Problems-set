nums = 101
original = nums
reversed = 0

while nums >0:
    digit = nums % 10
    reversed = reversed*10+digit
    nums = nums//10
if original == reversed:
    print("Yes the number is palindrome!")
else:
    print("No! The number is not palindrome")


 
