dict = {
    "Umair": 99,
    "Sudais": 67,
    "Shahid": 78,
           88: 89,
        " 3,=4.3": 56
}
 
swapped_data= {value: key for key,value in dict.items()}
print(swapped_data) # This method is good but for static case whenever we need to swape the random values in each other.
