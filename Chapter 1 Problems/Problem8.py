import os

for i in range(16, 18):
    a = os.path.join("Chapter 1 Problems",f"problem{i}.py")
    with open(a, "w")as f:
        print(a)


# import os

# for i in range(16, 18):
#     a = os.path.join("Chapter 1 Problems",f"Problem{i}.py")
#     if os.path.exists(a):
#         os.remove(a)
#         print(a)
# else:
#     print(f"Not found: {a}")
