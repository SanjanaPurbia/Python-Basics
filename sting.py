
city="Udaipur @19"
print(city)
# iterating string object
for ch in city:
    print(ch ,end="")
#indexing
print("\n",city[4])     #returns a char at given index
print(city[-5])
#ranging 
print(city[3:10])      #returns chars from 3 to 9
print(city[-9:-4])

#slicing
print(city[3: ])
print(city[ :15])
print(city[-6: ])

#concatenation
txt=city+"Rajasthan"
print(txt)

#repeatation
print(city*3)

#membership
if "smart" in "Udaipur is a smart city":
    print("yes,it is")
else:
    print("no,it is not")

#raw string
name="sp"
balance="2349.90"
year="2019:"
str = "Hello %s,\nYour bal is :\t%0.2f Rs\tin @%d year\b\bGood"\
        %(name,balance,year))
print(str)
str="Hello{},u can withdraw {}in {} year".format(name,balance,year)
print(str)
 