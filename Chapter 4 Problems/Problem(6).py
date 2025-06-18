Number_list= [1,3,4,5,6]
def missing_num(lst):
        n = len(lst) + 1
        expected_num = n*(n+1) //2
        usual_num = sum(Number_list)
        return expected_num - usual_num
missing_number = missing_num(Number_list)
print(missing_number) # This method is used for finding the missing number in the list.




Num_list= [1,3,4,5,6,8,10] # This is also recommended by me to use for missing numbers because you can you is in all perspectives of finding missing numbers.
def missing_num(lst):
        full_set = set(range(1,len(lst) +4))
        actual_set = set(lst)
        m_num = sorted(list(full_set - actual_set))
        return m_num
miss_num = missing_num(Num_list) # This is the ultimate method, used for finding any any range numbers, meanwhile for any number.
print(miss_num)     

        

