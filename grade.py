# to find grade/div based marks
Name=str(input("Enter your name: ") )
Math=int(input("Enter marks in maths(0-100):" ) )
Sci=int(input("Enter marks in sci(0-100):" ) )
Eng=int(input("Enter marks in eng(0-100):" ) )

if(Math<0 or Math>100 or Sci<0 or Sci>100 or Eng<0 or Eng>100):
  print("Marks are not in range")
else:
    avg=(Math+Sci+Eng)/3
    if avg>=80:
       print("topper and marks scored %0.2f %s marks" %(avg,'%') )
    elif avg>=60:
        print("first and marks scored %0.2f %s marks" %(avg,'%') ) 
    elif avg>=50:
        print("seconf and marks scored %0.2f %s marks" %(avg,'%') ) 
    elif avg>=40:
        print("third and marks scored %0.2f %s marks" %(avg,'%') ) 
    else:
        print("fail and marks scored %0.2 %s marks" %(avg,'%') ) 
print("this is your report card :) ")