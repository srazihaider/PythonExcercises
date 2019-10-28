#Write a Python program to display your details like name, age, address in three different lines. 
class Bio :
    
    def __init__(self, name, age, address) :
        self.name = name
        self.age = age
        self.address = address



a = Bio("razi",36,"my adress is hidden")
print(a.name)
print(a.age)
print(a.address)



