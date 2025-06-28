def classify_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not valid traingle!"
    elif a==b== c :
        return "The triangle is equiletral"
    elif a ==b or b ==c:
        return "The triangle is Isosceles"
    else:
        return "The traingle is scalene"
print(classify_triangle(9,9,3))