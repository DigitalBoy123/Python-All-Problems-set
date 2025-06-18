dict1 = {
    "Zulkarnain": 99,
    "Muib":89,
    "Yasit":34,
    "00": 12
}
dict2 = {
    "Muhammad": 766,
    "Nadim": 98,
    "Sudais": 78,
    "Karim Ali": 90,
    "Walid Khan": 34
}

dict3 = {
    "Muhammad": 88,
    "Jumad Ullah": 12,
    "Ubaid Ullah": 50,
    "Yasir": 100
}
# # The first method for merging multiple dictionaries in one.
merge_dicts = {**dict1, **dict2, **dict3}
print(merge_dicts)


# This is the second method for merging multiple dictionaries in one.
dict1.update(dict2)
dict1.update(dict3)

# This is the third method for merging multiple dictionaries.
merge_dicts = dict1 | dict2 | dict3
print(merge_dicts)

# This is the method in which we can include the same keys values.
merge_dic = {}
for key in set(list(dict1.keys()) +list(dict2.keys()) +list(dict3.keys())):
    merge_dic[key] = []
    if key in dict1:
        merge_dic[key].append(dict1[key])
    if key in dict2:
        merge_dic[key].append(dict2[key])
    if key in dict3:
        merge_dic[key].append(dict3[key])

print(merge_dic)





