#Writing a function is the function begins with "Is" return unchanged
#otherwise add "Is" to it
def string_modify(mystring) :
    if mystring[0:2] != "Is":
        return "Is"+mystring
    else:
        return mystring

print(string_modify("IsEmpty"))
print(string_modify("ramjaneis"))
