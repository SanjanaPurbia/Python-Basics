#defining a funtion 
def getbill(units):
    'to calc electricity bill'
    if units >=500:
        rate=7.5
    else:
        rate=5.0
    bill=units*rate
    print("bill is : %0.2f Rs" %bill)

#calling a func
getbill(700)
u=int(input("Enter Units : ") )
getbill(u)