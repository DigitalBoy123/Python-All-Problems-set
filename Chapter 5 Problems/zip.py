matrix = [[1,2,3],[4,5,6],[7,8,9]]
zip_matrix = list(zip(*matrix))
print(zip_matrix) # This is the case with transpose(change columns with rows).and



student_names = ["Saqi","Ali","Wahid","Jumad Ullah"]
Scores = [[33,44,23],[89,76,87],[98,75,87]]
# add_scores =  dict(zip(student_names,map(sum,Scores)))
for name,Scores in zip(student_names,Scores):
# print(add_scores)
   print(f"{name}:{sum(Scores)}")



fruits = ['cherry','grapes','orange']
quantities = [22,44,2]
prices =    [22,90,11]
calculate_costs = [] # Calculate the cost of fruits with their names
for q,p in zip(quantities,prices):
    calculate_costs.append(q*p)
for fruit,cost in zip(fruits,calculate_costs):
           print(f"{fruit}:{cost}")




zipped_list = [['a',1],['b',2],['c',3]]
fruits,cost= zip(*zipped_list)
print(fruits)
print(cost)

for i in range(1,16):
    t = f"Chapter 6 Problems/Problem({i}).py"
    with open(t, "w")as f:
        print(t)
         
      


