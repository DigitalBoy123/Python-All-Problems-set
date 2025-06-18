def Check_anagrams(s,g):
    return sorted(s) == sorted(g)
s = "teacher"
g = "cheater"
print(Check_anagrams(s,g))