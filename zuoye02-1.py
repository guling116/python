'''
#EP-10
import random
a=random.randrange(0,100)
b=random.randrange(0,100)
n=eval(input("shu ru yi ge shu : "))
if(n==(a+b)):
    print(True)
else:
    print(False)
'''
'''
#EP-11
a=eval(input("Enter today's 0--6 : :"))
b=eval(input("Enter the number of day elapsed since today :"))
c=["Sun","Mo","Tuesday","Wed","Thursday","Firday","Saturday"]
if((a+b)%7==0):
    d=c[0]
elif((a+b)%7==1):
    d=c[1]
elif((a+b)%7==2):
    d=c[2]
elif((a+b)%7==3):
    d=c[3]
elif((a+b)%7==4):
    d=c[4]
elif((a+b)%7==5):
    d=c[5]
else:
    d=[6]
x=c[a]
print("Today is {} and the futher day is {}".format(x,d))
'''

'''
#EP-12
x,y,z=eval(input("shu ru san ge shu : "))
a=[x,y,z]
a.sort()
print(a)
'''
'''
#EP-13
a,b=eval(input("Enter weight and price for package 1 :"))
a1,b1=eval(input("Enter weight and price for package 2 :"))
if(b/a>b1/a1):
    print("package 2 has the batter pice")
elif(b/a==b1/a1):
    print("package 2 = 1")
else:
    print("package 1 has the batter pice")
'''
'''
#EP-14
a,b=eval(input("shu ru yuefen he nianfen :"))
a=[1,2,3,4,5,6,7,8,9,10,11,12]
'''





