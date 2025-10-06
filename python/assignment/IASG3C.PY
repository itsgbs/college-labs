#program for quadratic equation
# import math
a = float(input("Enter the value of a "))
b = float(input("Enter the value of b "))
c = float(input("Enter the value of c "))

if(a!=0):

    discriminant = b**2 - 4 * a * c
    
    if(discriminant==0):
        root = -b/(2*a)
        print(f"The two equal roots are : {root} and {root}")

    else:
        root1 = (-b + discriminant**0.5)/(2*a)
        root2 = (-b - discriminant**0.5)/(2*a)
        if(discriminant>0):
            print(f"The two distinct real roots are {root1:.3f} and {root2:.3f}")
        else:
            # imaginarypart = math.sqrt(-discriminant) / (2*a)
            print(f"The complex roots are {root1:.3f} and {root2:.3f}")
else:
    print("a value is invalid")
    