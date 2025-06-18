t = "Mohamad Ali was very good person and he was looking vey gorgeous"
r = t.split()
y = {}
for word in r:
     
    if word in y:
         
        y[word]+= 1
    else:
        y[word] =1
for word, count in y.items():
    print(f"{word}: {count}")

     
        
    
     
    