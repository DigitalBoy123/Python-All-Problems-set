Flattened_L = [1,2,3,[4,5,6,],[7,8,[9,10]]]
def flattened_list(Flattened_L):
    flattened_List = []
    for item in Flattened_L:
        if isinstance(item,list):
            flattened_List.extend(flattened_list(item))
        else:
            flattened_List.append(item)
    return flattened_List
print(flattened_list(Flattened_L))