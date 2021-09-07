try:
    age= int(input("Enter the age:"))
    if(age>=18):
        print("eligible for vote")
    else:
        print("not eligible")
except:
    print("Plz enter valid age")