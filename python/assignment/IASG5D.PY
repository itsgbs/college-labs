str = input("Enter the string ")
pos1 = int(input("Enter the 1st position "))
pos2 = int(input("Enter the 2nd position "))
substr = str[pos1-1:pos2]
print(substr)

k = len(substr)
reverse = substr[-1:-(k+1):-1]
print(reverse)

if substr==reverse:
    print("String is palindrome")
else:
    print("String is not palindrome")