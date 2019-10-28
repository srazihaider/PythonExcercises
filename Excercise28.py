#28. Write a Python program to print all even numbers from a given numbers list in the same order and 
# stop the printing if any numbers that come after 237 in the sequence. Go to the editor

def evennumber_in_list(mylist):
    even_list=[]
    for i in mylist :
        if i>237 :
            break
        elif i%2 == 0:
            
            even_list.append(i)
        return even_list

print(evennumber_in_list([1,2,3,4,5,6,7,8,9,10]))       