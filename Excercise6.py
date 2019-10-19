mycomma_seperated = input("Enter a comma seperated list of values")
mylist = mycomma_seperated.split(",")
mylist = list(map(int,mylist))  #maps the values from string to int
print(mylist)
mytuple = tuple(mylist)
print(mytuple)