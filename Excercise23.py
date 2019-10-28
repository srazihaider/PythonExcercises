def return_copy_string(mystring, n):
    if len(mystring)>2 :
        return n*mystring[:2]
    else:
        return n*mystring

print(return_copy_string("paparazi",4))
print(return_copy_string("zi",4))


    