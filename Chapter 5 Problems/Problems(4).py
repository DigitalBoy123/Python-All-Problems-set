dict = {
    "Umair": 99,
    "Sudais": 67,
    "Shahid": 78,
           88: 89,
          " 3,=4.3": 56
}
freq ={}
for key,value in dict.items():
    for chr in str(key) + str(value):
        if chr in freq:
            freq[chr] += 1
        else:
            freq[chr] =1
print(freq)





 