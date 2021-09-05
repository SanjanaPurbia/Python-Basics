str="tech is BEST @19 #101"
    #methods
#returns size of given str
size=len(str)
print(size)

#returns an index of given str
print(str.index("@19") )

#checking all chars are alphabets or digits
print(str.isalnum() )

#checking all chars are alphabets 
print(str.isalpha() )

#checking all chars are digits
print(str.isdigit() )

#checking all chars are digits
print("5050".isdigit() )

#checking all chars are in upper case
print(str.isupper() )

#checking all chars are in lower case
print(str.islower() )

#checking all chars are space
print(" ".isspace() )

#replecing old str with new new str
print(str.replace("@19",'@2019') )

#capitalize
print(str.capitalize() )

#swapping case
print(str.swapcase() )

#counting no of occurances
print(str.count('1') )

#splitting str by delimiter 
tokens= str.split(" ")
print(tokens)
