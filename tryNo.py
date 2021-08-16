try:
    n=int(input("enter no:"))
    if n>=0:
        print("no is=",n)
    else:
        raise ValueError("value is less then zero")
except ValueError as ex:
    print(ex)