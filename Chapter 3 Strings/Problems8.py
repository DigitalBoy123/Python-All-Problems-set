import string
s = "The most crucial thing is to be Emphathetic!"
translator = str.maketrans('','',string.punctuation)
f = s.translate(translator)
print(f)