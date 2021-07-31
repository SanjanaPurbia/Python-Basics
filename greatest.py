# to find the largest among 3 no
x=float(input("enter x:"))
y=float(input("enter y:"))
z=float(input("enter z:"))

if x>y:
    if x>z:  
         print("x= %0.2f is large" %x)
    else:
         print("z= %0.2f is large" %z)
else:
    if y>z:
         print("y= %0.2f is large" %y)
    else:
         print("z= %0.2f is large" %z)
print("end")