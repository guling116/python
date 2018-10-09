#class joker:
#    a=10
#if __name__ == '__main__':
#    print joker.a


'''
class joker:
    def __init__(self):  #chu shi hua
        print("hhhhh")
if __name__ == '__main__':
    joker()
'''
'''
class joker:
    def __init__(self):
         self.h='truet'
         self.l='lflash'
    def a(self):
         print self.h
         print self.l
if __name__ == '__main__':
    joker().self.h
'''


'''
class ep1():
    def __init__(self):
        self.sum=1001
        print("init over")
    def a(self):
        if self.sum % 2 ==0:
            print("oushu")
        else:
            print("jishu")
if __name__ == '__main__':
    ep1().a()
'''





'''
class ep2:
    def __init__(self):
        self.sum=10
        print("init over")
    def num_2(self):
        NUM2=self.sum ** 2
        self.sum=NUM2
        print(self.sum)
    def num_3(self):
        self.sum=self.sum ** 3
        print(self.sum)
if __name__ == '__main__':
    a=ep2()
    a.num_2()
    a.num_3()
'''

'''
class ep3:
    def __init__(self,sum2):
        self.sum=sum2
        print("init over")
    def num_2(self,b):
        NUM2=self.sum ** 2 + b
        self.sum=NUM2
        print(self.sum)
    def num_3(self,c):
        self.sum=self.sum ** 3 + c
        print(self.sum)
if __name__ == '__main__':
    a=ep3(8)
    a.num_2(10)
    a.num_3(10)
'''
'''
class mayun:
    def __init__(self):
        self.caichan = 1000000
    def show(self):
        print self.caichan
class niu(mayun):
    def __init__(self):
        mayun.__init__(self)
        self.niu =10
    def showniu(self):
        print ("jicheng",self.caichan)
niu().showniu()
'''

class Circle:
    def __init__(self,width,height):
        self.a=width
        self.b=height
    def getArea(self):
        Area=self.a * self.b
        print(Area)
    def Perimeter(self):
        Perimeter=(self.a + self.b) * 2
        print(Perimeter)
#class RE(Circle):
#    def __init__(self,width,height):
#        Circle.__init__(self,width,height)
#    def TWO(self):
#        print



if __name__ == '__main__':
    a=Circle(4,40)
    a.getArea()
    a.Perimeter()











