def first_letter_capital(r):
       t = r.split()
       y = []
       for word in t:
                 i = word[0].upper() + word[1:].lower()
                 y.append(i)
       return  ' '.join(y)
     



r = "hani khanan" 
print(first_letter_capital(r))