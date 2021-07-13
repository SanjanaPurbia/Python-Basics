# creating a dict to store emp details 
empInfo={12001:'Ganeshn',12003:"pragya",12002:"Bhavesh"}
print(empInfo)

#iterating a dict
for item in empInfo:
    print(item," : ",empInfo[item] )
#adding new item 
empInfo[12004]="Sagar"
print(empInfo)

#update an item 
empInfo[12003]="pritam"
print(empInfo)

#delete an item 
del empInfo[12001]
print(empInfo)

#searching an item by key 
print(empInfo[12003] )

#function 
#returns size of dict 
print(len(empInfo) )
print(str(empInfo) )