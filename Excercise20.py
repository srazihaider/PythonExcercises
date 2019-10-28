#Write a function that takes 2 inputs
#1) A string (mystring)
#2) Number of Copies(n)
#Now the function should return a string such that it is copied n times
#i.e RepeatRepeatRepeat if mystring is Repeat and n is 3

def repeat_string(mystring,n) :
    Concat=""
    for i in range(n) :
        Concat = mystring+Concat
    return Concat
print(repeat_string("Repeat",3))
print(repeat_string("Repeat",5))