#I have implemented the following algorithm using the euclidean method which suggests to recursively keep taking
# the GCD by replacing b with a and b with a%b until we reach a point where b becomes zero at this point 
# a would be the answer
# I used the following video to revise the algorithm https://www.youtube.com/watch?v=VWOUh4w_zVI

def Greatest_Common_Devisor(a,b) :
    if b==0 :
        return a
    else :
        return Greatest_Common_Devisor(b,a%b)

print(Greatest_Common_Devisor(15,45))
print(Greatest_Common_Devisor(45,15))
print(Greatest_Common_Devisor(4,6))