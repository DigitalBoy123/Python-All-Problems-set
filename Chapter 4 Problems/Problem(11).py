List = [1,2,3,44,66,55,44,3,64,3]
element = 44
print(List.count(element))


from collections import Counter
List = [1,22,3,4,5,66,5,4]
freq = Counter(List)
for num, count in freq.items():
            print(f"number:({num}) occurance:({count})")# This is the second method for frequency counting of each element in a lilst.

 
List = [1,22,3,4,5,66,5,4] # This is the first method for frequency counting of each element in a lilst.
for num in set(List):
        y = List.count(num)
        print(f"number:({num}) occurance:({y})")


 