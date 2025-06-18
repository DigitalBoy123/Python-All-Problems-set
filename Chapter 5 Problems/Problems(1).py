dicionary_no1 = {
    "Naveed": 89,
    "Jummad": 99,
    "Niamat": 90,
    "Jameel": 23

}
dicionary_no2 = {
    "Hussain": 90,
    "Imadad": 23,
    "Yaseen": 99,
}
# Using the update method.
dicionary_no1.update(dicionary_no2)
print(dicionary_no1) # This is the first method for merging two dctionaries.

# Using the method of double stars operator.
merge_dic = {**dicionary_no1,**dicionary_no2}
print(merge_dic) # This is the second method for merging two dictionaries.



# This is the problem to solve with the given problem for building the logical skill of solving problems from my own self.
dict1 = {
    "Muhammad": 88,
    "Nadim": 98,
    "Sudais": 78,
    "Karim Ali": 90,
    "Walid Khan": 34
}

dict2 = {
    "Muhammad": 88,
    "Jumad Ullah": 12,
    "Ubaid Ullah": 50,
    "Yasir": 100
}

dict1.update(dict2)
print(dict1)


# This method is used when we wanna not to effect the dictionary or make changes in the dictionary.
dict1 = {
    "Muhammad": 88,
    "Nadim": 98,
    "Sudais": 78,
    "Karim Ali": 90,
    "Walid Khan": 34
}

dict2 = {
    "Muhammad": 88,
    "Jumad Ullah": 12,
    "Ubaid Ullah": 50,
    "Yasir": 100
}
merge_dic = dict1.copy()
merge_dic.update(dict2)
print(merge_dic)
