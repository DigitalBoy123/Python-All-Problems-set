List = [1,2,3,44,66,55,44,3,64,3]
even_numbers = []
odd_numbers = []
for num in List:
    if num % 2 ==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even number:", even_numbers)
print("Odd numbers:",odd_numbers)


    