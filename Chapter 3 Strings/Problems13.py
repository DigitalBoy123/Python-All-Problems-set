import base64
# string =   input("Enter your string: ")
# encode_string = string.encode('utf-8')
# unicode_string=base64.b64encode(encode_string).decode('utf-8')
# print(unicode_string)

bytes_string = "SWYgeW91IHdhbm5hIHRvIGxlYXJuIHNvbWV0aGluZyBuZXcgaW4geW91ciBmaWVsZCB0aGVuIGFsd2F5cyB0cnkgbmV3IHRoaWdzIGluIHlvdXIgZmllbGQsIG1lYW53aGlsZSBpZiB5b3VyIGFwcHJvYWNoIGlzIHJlbGF0ZWQgdG8gbGltaXRlZCB0aGluZyBpbiB5b3VyIHRhc2sgdGhlbiB0cnkgdG8gZXhwbG9yZSBuZXcgdGhpbmdzLg=="
encode_string = base64.b64decode(bytes_string)
encode_bytes= encode_string.decode("utf-8")
print(encode_bytes)
 


