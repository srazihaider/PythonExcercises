# Function to input a list and count the number 4 in that list and return
# the value

def Count4(mylist) :
        count=0
        for i in mylist: 
                if i==4 :
                        count+=1
        return count
    
print(Count4([1, 4, 6, 7, 4]))
