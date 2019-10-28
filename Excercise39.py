# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
# this program could be written in a much easier way but I wanted to practice classes, constructors and recurssion in one program

class Money_Matters :
    def  __init__(self,principle_amount,rate_of_interest, years):
        self.principle_amount = principle_amount
        self.rate_of_interest = rate_of_interest
        self.years = years
        self.principle_amount_that_year = principle_amount

    def future_value(self,principle_amount,myyear) :
        if myyear == 0 :
            return self.principle_amount_that_year
        else :
            myyear = myyear-1
            self.principle_amount_that_year = (1+ self.rate_of_interest/100)*self.principle_amount_that_year
            return  self.future_value(self.principle_amount_that_year,myyear)
            


a=  Money_Matters(10000,3.5,7)
print(a.future_value(a.principle_amount,a.years))
