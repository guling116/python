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
#4-3.
class Fan:
    def __init__(self,speed=1,on=False,radius=5,color='blue',):
        self.SLOW=1
        self.MEDIUM=2
        self.FAST=3
        self.__speed=int(speed)
        self.__on=bool(on)
        self.__radius=float(radius)
        self.__color=str(color)
        print("speed is {},on is {} ,radius is {},color is {}".format(self.__speed,self.__on,self.__radius,self.__color))
Fan(3,not False,10,'yellow')
Fan(2,False,5,'blue')
'''

#4-4
class LE:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getx(self):
        x = ((self._LE__e*self._LE__d)-(self._LE__b*self._LE__f))/((self._LE__a*self._LE__d)-(self._LE__b*self._LE__c))
        print(x)
    def gety(self):
        y = ((self._LE__a*self._LE__f)-(self._LE__e*self._LE__c))/((self._LE__a*self._LE__d)-(self._LE__b*self._LE__c))
        print(y)
a,b,c,d,e,f = eval(raw_input(">>"))
if a*d-b*c==0:
    print("no")
else:
    LE(a,b,c,d,e,f).getx()
    LE(a,b,c,d,e,f).gety()
'''

'''
#4-5
import math
class LE:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getx(self):
        x = (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        print(x)
    def gety(self):
        y = (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
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






