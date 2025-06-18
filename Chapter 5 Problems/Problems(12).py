str = "I amn't the person about who you are thinking everyday!"
def longest_word():
    words = str.split()
    max_word =max(words,key=len)
    return max_word
print(longest_word()) 
 