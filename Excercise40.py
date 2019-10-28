#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
#again to learn about classes I especially created a Cartisian Coordinate Class and later defined a function for interaction of
# the attributes of the two objects to finalize my result

class Cartesian_Coordinates : 
    def __init__(self,x,y) :
        self.x = x
        self.y = y

def total_distance(a,b) :
    return ((a.y - b.y)**2 + (a.x - b.x)**2) **0.5

a = Cartesian_Coordinates(-7,-4)
b = Cartesian_Coordinates(17,6.5) 
print(total_distance(a,b))



        



