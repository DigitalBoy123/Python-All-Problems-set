def rotating_num(lst,n):
    t = n % len(lst)
    return lst[-n:] + lst[:-n]
lst = [1,2,3,4,5,6,7,8,9,10]
n = 9
print(rotating_num(lst,n))