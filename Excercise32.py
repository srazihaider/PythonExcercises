def Greatest_Common_Devisor(a,b) :
    if b==0 :
        return a
    else :
        return Greatest_Common_Devisor(b,a%b)


def Least_Common_Multiple(a,b) :
    return abs(a*b)/Greatest_Common_Devisor(a,b)

print (Least_Common_Multiple(30,40))
print (Least_Common_Multiple(100,50))
