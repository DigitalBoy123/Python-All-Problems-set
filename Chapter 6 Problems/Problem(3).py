str1 = "Munir"
str2 = "Karim Khan"
def check_lexicography():
    if str1 < str2:
        return f"{str1} comes before {str2}"
    elif str1>str2:
        return f"{str1} comes after {str2}" 
    else:
        return "Both are same!"
print(check_lexicography())




str1 = "Munir"
str2 = "Karim Khan"
def check_lexicography(str1,str2):
    if str1 < str2:
        return f"{str1} comes before {str2}"
    elif str1>str2:
        return f"{str1} comes after {str2}" 
    else:
        return "Both are same!"
print(check_lexicography(str1,str2))






def check_lexicography(str1,str2):
    if str1 < str2:
        return f"{str1} comes before {str2}"
    elif str1>str2:
        return f"{str1} comes after {str2}" 
    else:
        return "Both are same!"
print(check_lexicography( "Munir","Karim Khan"  ))




def check_lexicography(*args):
    str1,str2=args
    if str1 < str2:
        return f"{str1} comes before {str2}"
    elif str1>str2:
        return f"{str1} comes after {str2}" 
    else:
        return "Both are same!"
print(check_lexicography("Hasham","Gulkhan"))



def check_lexicography(str1,str2):
    if str1 < str2:
        return f"{str1} comes before {str2}"
    elif str1>str2:
        return f"{str1} comes after {str2}" 
    else:
        return "Both are same!"
print(check_lexicography("Muhammad","Umair"))




# This is the method of class for solving the problme
class  check_lexicography:
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2

    def compare_str(self):
        if self.str1 < self.str2:
            return f"{self.str1} comes before {self.str2}"
        elif str1>str2:
            return f"{self.str1} comes after {self.str2}" 
        else:
            return "Both are same!"
comparator = check_lexicography("Munir","Yasir")
print(comparator.compare_str())
