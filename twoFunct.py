def values():
    x=10
    def inner():
        x=0
        print(x)

    inner()
    print(x)
    
values()