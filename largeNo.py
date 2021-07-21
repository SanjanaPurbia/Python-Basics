l = int(input("Enter number (grater than three digit number):-"))
if l >=3:
    k = str(l)
    k = int(k[-2])
    print(k)
else:
    print("Number have less than three digit")