def reversed_list(r):
    reversed_list = []
    for i in range(len(r) -1,-1,-1):
        reversed_list.append(r[i])
    return reversed_list
r = ["Akram","Nadeem","Sudais","Jamal","Wahid"]
print(reversed_list(r))
         