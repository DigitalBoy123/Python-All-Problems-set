t = "He is the man of good thinking and also does good for people"
vowels =" aeiou"
count = 0
for char in t.lower():
    if char in vowels:
        count += 1
print(count)


