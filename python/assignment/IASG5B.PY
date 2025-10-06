str = input("Enter the string ")
roll = ""
name = ""
#FOR NUMBERS IN THE STRING
# for char in str:
#     if('0'<=char<='9'):
#         roll += char
#with use of function
pos = str.find('@')
roll = str[:pos]
print(roll,end=" ")

#for mckvie to MCKVIE
# for i in range(str.find('@')+1,str.find('.')):
#     # name+=chr(ord(str[i])-32)
#     name+=str[i].upper()
name = str[str.find('@')+1:str.find('.')].upper()

print(name)