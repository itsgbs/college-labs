sen = input("Enter the String ")
new_sen = ""
Upp = Low = 0
for char in sen:
    if 65<=(ord(char))<=90:
        Upp+=1
    elif 97<=(ord(char))<=122:
        Low+=1
print("number of uppercase ",Upp)
print("number of lowercase ",Low)