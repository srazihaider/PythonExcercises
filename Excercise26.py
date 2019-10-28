def myhistogram(mylist):
    hist = ""
    for i in mylist:
        for i in range(0,i) :
            hist= hist + "*"
            hist= hist + " "
        print(hist)             

myhistogram([2,4,6,8,9,10])


