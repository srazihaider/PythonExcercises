#Write a Python program to add two objects if both objects are an integer type
def sum_of_objects(a,b):
    sum = a+b
    if type(a).__name__== "int" and type(b).__name__ == "int" :
        return sum
    else:
        return "sum only for int type"

print(sum_of_objects("abc","def"))
print(sum_of_objects(20,10))



