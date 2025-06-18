q = int(input("Enter your Temperature: "))
def f_to_c(q):
    return 5*(q-32)/9
g = f_to_c(q)
print(f"{round(g,2)}°C")