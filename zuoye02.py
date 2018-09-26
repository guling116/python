#EP-1
'''
import math
r =eval(input("Enter the length from the center to a vertex>>"))
s=2*r*math.sin(math.pi/5)
A=5*s*s/(4*math.tan(math.pi/5))
print("The area of the pentagon is %.2f "%A)
'''

'''
#EP-2
import math
x1,y1=eval(input("Enter point 1(latitude and longitude) in degrees >>"))
x2,y2=eval(input("Enter point 2 (latitude and longitude) in degrees >>"))
d=6371.01*(math.acos((math.sin(math.radians(x1))*math.sin(math.radians(x2))+math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1-y2)))))
print("The distance between the two points is ",d)
'''
'''
#EP-3
import math
s=eval(input("Enter the side :"))
A=(5*s*s)/(4*math.tan(math.pi/5))
print("The area of the pentagon is ",A)
'''
'''
#EP-4
import math
n=eval(input("Enter the number of inside :"))
s=eval(input("Enter the side :"))
A=(n*pow(s,2))/(4*math.tan(math.pi/n))
print("The area of the polygon is ",A)
'''
'''
#EP-5
import math
a=eval(input("Enter an ASCII code "))
if (a>0 and a<=107):
    print("The character is ",chr(a))
else:
    print("输入有误")
'''

'''
#EP-6
inf=input("Enter employee's name :")
hour=eval(input("Enter number of hours works in a week :"))
rate=eval(input("Enter hourly pay rate :"))
fed=eval(input("Enter federal tax withholding rate :"))
state=eval(input("Enter state tax withholding raee :"))
A=hour*rate
B=hour*rate*0.2
C=hour*rate*0.09
print("Enter employee's name :",inf)
print("Hours Worked ",hour)
print("Pay Rate ",rate)
print("Gross Pay",A)
print("Deductions : Federal Withholding(20%)",B)
print("State Withholding(9.0%):",C)
print("Total Deduction ",B+C)
print("Net Pay",A-(B+C))
'''

'''
#EP-7
a=input("Enter an integer :")
print("The reversed number is " ,a[::-1])
'''
'''
#EP-8
a=input("Enter the number :")
chr(ord(a)+1)
'''



#EP-9
import math
a,b,c=eval(input("Enter a , b , c :"))
A=b*b-4*a*c
if(A>0):
    r1=(-b+math.sqrt(A))/2*a
    r2=(-b-math.sqrt(A))/2*a
    print("THe roots are ",r1,r2)
a,b,c=eval(input("Enter a , b , c :"))
elif(A==0):
    r1=(-b+math.sqrt(A))/2*a
    print("The roots are",r1)
a,b,c=eval(input("Enter a , b , c :"))
else:
    print("The equation has no real root")


