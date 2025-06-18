List1 = ["Sadeeq", "Nadeem","Halaq", "Niamat", "walid"]
List2 = ["Halaq","Niamat", "Wasay","Zukairam"]
# We use the method of & operator to use it like intersection.
common_elements = set(List1) & set(List2)
print(common_elements)




List1 = ["Sadeeq", "Nadeem","Halaq", "Niamat", "walid"]
List2 = ["Halaq","Niamat", "Wasay","Zukairam"]
set1 = set(List1)
set2 = set(List2)
common_elements = set1.intersection(set2)
print(common_elements) # This is the second way to check the repeated elements in two lists.





List1 = ["Sadeeq", "Nadeem","Halaq", "Niamat", "walid"] # This is the long method for repeated elements cheking.
List2 = ["Halaq","Niamat", "Wasay","Zukairam"]
def Repeated_elements(List1,List2):
    List3 = []
    for element in List1:
        if element in List2:
            List3.append(element)
    if List3:
            return List3
    else:
       return "No the elements not found"
print(Repeated_elements(List1,List2))
                   

     


