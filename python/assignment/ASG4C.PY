print("all two digit automorphic numbers are : ",end="")
for x in range(10,100):
    if(x == x**2 % 100):
        print(x,end=" ")