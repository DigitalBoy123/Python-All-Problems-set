List = [1,22,3,4,5,66,5,4]
max_num = max(List)
List.remove(max_num)
New_num = max(List)
print(New_num)

List = [1,22,3,4,5,66,5,4]
Second_num = max(x for x in List if x != max(List))
print(Second_num)
