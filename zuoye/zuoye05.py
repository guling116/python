'''
class Account:
    def __init__(self,idname,balance,annua):
        self.__a=int(idname)
        self.__b=float(balance)
        self.__c=float(annua)
        print(self.__a)
    def getMonthlyInterestRate(self):
        self.Monre=(self.__ann/12)*self.d
        print(self.Monre)
    def getMonthlyInterest(self):
        self.Mon=self.__ann/12
        print(self.Mon)
    def withdraw(self,a):
        self.w=self.__balance-a
    def deposit(self,b):
        self.d=self.w+b
        print(self.d)

if __name__ == '__main__':
    a=Account(1122,20000,0.045)
    a.getMonthlyInterest()
    a.winthdraw(2500)
    a.deposit(3000)
    a.getMothlyInterestRate()
'''
'''
#4-1-1
class Account:
    def __init__(self,idname=0,balance=100,annua=0):
        self.__id=int(idname)
        self.__balance=float(balance)
        self.__ann=float(annua)
        print(self.__id)
    def getMon(self):
        self.Mon=self.__ann/12
        print(self.Mon)
    def winthdraw(self,a):
        self.w=self.__balance-a
    def deposit(self,b):
        self.d=self.w+b
        print(self.d)
    def getMonre(self):
        self.Monre=(self.__ann/12)*self.d
        print(self.Monre)
a=Account(1122,20000,0.045)
a.getMon()
a.winthdraw(2500)
a.deposit(3000)
a.getMonre()
'''
'''
#4-2
import math
class Regul:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__a=int(n)
        self.__b=float(side)
        self.__c=float(x)
        self.__d=float(y)
    def getPerimeter(self):
        self.e=self.__a * self.__b
        print("duo bian zhou chang {}".format(self.e))
    def Area(self):
        self.s=self.__b*self.__b
        self.t=(math.sin(math.pi/self.__a))/(math.cos(math.pi/self.__a))
        self.y=(self.__a*self.s)/4*self.t
        print("the duo bian xing area is {}".format(self.y))
Regul().getPerimeter()
Regul().Area()
Regul(x=6,y=4).getPerimeter()
Regul(x=6,y=4).Area()
Regul(10,4,5.6,7.8).getPerimeter()
Regul(10,4,5.6,7.8).Area()
'''
'''
#4-3.
class fan:
    def __init__(self,speed=1,on=False,radius=5,color="blue"):
        self.speed=speed
        self.on=on
        self.radius=radius
        self.color=color
    def show(self):
        print("speed is {},on is {} ,radius is {},color is {}".format(self.speed,self.on,self.radius,self.color))
fan(3,not False,10,'yellow').show()
'''
'''
#4-4
class Li:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
    def isSo(self):
        self.z=(self.a * self.d)-(self.b * self.c)
        if (self.z!=0):
            return True
        else:
            print("False")

    def getX(self):
        self.x=((self.e * self.d)-(self.b * self.f))/self.z
        print(self.x)
    def getY(self):
        self.y=((self.a * self.f)-(self.e*self.c))/self.z
        print(self.y)
a,b,c,d,e,f=eval(raw_input(">>"))
g=Li(a,b,c,d,e,f)
if(g.isSo()==True):
    g.getX()
    g.getY()

'''
'''
#4-5
import math
class LE:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def getx(self):
        x = (self.e*self.d-self.b*self.f)/(self.a*self.d-self.b*self.c)
        print(x)
    def gety(self):
        y = (self.a*self.f-self.e*self.c)/(self.a*self.d-self.b*self.c)
        print(y)
x1,y1,x2,y2=eval(raw_input("Enter the endpoints of the first line segment:"))
x3,y3,x4,y4=eval(raw_input("Enter the endpoints of the second line segment:"))
a = y1 - y2
b = x2 - x1
e = x2*y1-x1*y2
c = y3 - y4
d = x4 - x3
f = x4*y3-x3*y4
if a*d-b*c==0:
    print("no")
else:
    LE(a,b,c,d,e,f).getx()
    LE(a,b,c,d,e,f).gety()
'''

class Li:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
    def getX(self):
        self.x=((self.e * self.d)-(self.b * self.f))/(self.a*self.d-self.b*self.c)
        print(self.x)
    def getY(self):
        self.y=((self.a * self.f)-(self.e*self.c))/(self.a*self.d-self.b*self.c)
        print(self.y)
a,b,c,d,e,f=eval(raw_input(">>"))
if a*d-b*c==0:
    print("no")
else:
    Li(a,b,c,d,e,f).getX()
    Li(a,b,c,d,e,f).getY()






