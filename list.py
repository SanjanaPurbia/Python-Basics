x=[]
lst=input("Enter list elements:")
def number(x):
    for i in lst:
        if i not in x:
            x.append(lst)
        return x
print(number(lst))
        