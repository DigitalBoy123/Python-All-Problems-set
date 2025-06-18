Main_string= "Hey my jaan1 where do you leeve!"
sub_string = "live"
index = Main_string.find(sub_string)
if index != -1:
    print(f"The {sub_string} found at: ({index})") 
else:
    print("The sub_string not found!")