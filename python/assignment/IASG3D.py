# print("Enter a character\n")
char = input("Enter a character: ")
vowels = 'aeiouAEIOU'

# if char.isalpha() and len(char) == 1:
#     if char in vowels:
#         print("It's a vowel.")
#     else:
#         print("It's a consonant.")
# else:
#     print("Invalid input.")

match char:
    case _ if char in vowels:
        print(f"{char } is a vowel")
    case _ if (char.isalpha() and len(char)==1 ):
        print(f"{char} is a consonant")
    case _: 
        print("invalid input ")