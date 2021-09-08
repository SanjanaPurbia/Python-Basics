#list methods example
names=["sanjana","hrishita","shruti","manish","kamlesh"]
print(names)

#adding/appending new item
names.append("ram")
print(names)

#returning no of occurance of given item
print(names.count("kamlesh") )

#returns an index of given of given item
print(names.index("manish") )

#extending a list 
names.extend(["jadu","dada"])
print (names)

#inserting an item at given index
names.insert(2,"sonu")
print(names)

#removing an item from given item 
names.pop()
print(names)

#removing a given item 
names.remove("manish")
print (names)

#reversing a list
names.reverse()
print(names)

#sorting a list in given order
names.sort(reverse=True)
print(names)

#copying a list
print(names.copy() )

