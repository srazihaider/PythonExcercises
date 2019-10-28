#Write a Python program to print out a set containing all the colors 
#from color_list_1 which are not present in color_list_2. Go to the editor

def color_diff(color_list_1, color_list_2) :
    return [item for item in color_list_1 if item not in color_list_2]

print(color_diff(["White","Green","Yellow"],["Yellow","Green","Black"]))