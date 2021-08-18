#creating a tuple to store marks 
marks=(92,67,89,90,92,76)
print(marks)

#iterating a tuple
for item in marks:
  print(item)

#add/remove/update
#del marks[2]
#functions
print(len(marks))
print(max(marks))
print(min(marks))
t=tuple("TECHNO")
print(t)

#methods
print(marks.count(92) )
print(marks.index(90) )