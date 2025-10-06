sen = input("Enter the String ")
new_sen = ""
for char in sen:
    if 65<=(ord(char))<=90:
        new_sen += chr(ord(char)+32)
    elif 97<=(ord(char))<=122:
        new_sen += chr(ord(char)-32)
    else:
        new_sen += char
print("new string ",new_sen)
