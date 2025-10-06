#1/1! + 2/2! ... till 7 terms
print("The sum of first seven terms are ",end="")
sum = 0
for i in range(1,8):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum = sum + i/fact
print(sum)