lst=input("Enter list elements:")
def number(lst):
    x=[]
    for i in lst:
        if i not in x:
            x.append(i)
    return x
print(number(lst))