#check list is palindrome or not
list1 = [1,2,3,2,2]
list2 = list1.copy()
list2.reverse()
if(list1==list2):
    print(f"{list1} is a palindrome")
else:
    print(f"{list1} is a not palindrome")