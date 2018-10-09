"""#4-1
from __future__ import print_function
def getPentagoalNumber(n):
    for i in range(1,n):
        s = (i*(3*i-1))/2
        print(s,end=" ")
        if i%10==0:
            print("")
getPentagoalNumber(100)
"""

#4-2
from __future__ import print_function
def sumDigits(n):
    a=n/100
    b=n%100/10
    c=n%100%10
    d=a+b+c
    print("zheng shu he ".format(d))
a=eval(input("shuruyige hu:"))
sumDigits(a)

