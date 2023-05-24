def parrot(string = "Squawk!"):
    for i in string:
        print(string)
        return string

parrot("hello")

#The parrot() function should accept an argument of a string 
#and both print() and 
#return the 
#string at the 
#end of the function.

#The parrot() function should have a default argument of "Squawk!"

#NOTE: This lab is explicitly testing your ability to control 
#the return value of a function: 
#not just what it does, 
#but what it returns. 
#Remember, return values are important.
#What's the return value of print()?