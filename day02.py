#1  pow(x,y,z) 表示为(x**Y)%z
#2  round(0.147,2) 表示为0.147 保留两位小数
#3  math.ceil()向上取整  math.floor（）向下取整
#4    math.log()默认e为底   math.log(10,10)不启用默认
#5  ord() 返回ascii值  chr()返回对应字符 sqrt()开方
'''
#求三角形个角度度数
import math
x,y,x1,y1,x2,y2=eval(input("shu ru >>"))
a=math.sqrt(pow(x1-x,2)+pow(y1-y,2))
b=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
c=math.sqrt(pow(x-x2,2)+pow(y-y1,2))
A=math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
B=math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
C=math.degrees(math.acos((c*c-b*b-a*a)/(-2*a*b)))
print("三个角度为 ",A,B,C)


import math
x1, y1 = eval(input('输入A点坐标：'))
x2, y2 = eval(input('输入B点坐标：'))
x3, y3 = eval(input('输入C点坐标：'))
a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))
print('三角形的三个角分别为', A, B, C)
'''
'''
a="welcome"
b="python"
print(a+b)
str(100) + "joke is a good man"
'''
'''
a=int(input("shuruyigeshu>>"))
if a%2==0:
    print('o')
else:
    print('ji')
'''

'''
name=input("相不相亲 1 or 0(1 同意  0 不同意 )>>")
if (int(input("帅不帅>>"))==1):
    if (int(input("有没有钱>>"))==1):
        if (int (input ("有没有老婆>>"))==1):
            if (int (input("有没有房>>"))==1):
                print("可以见一下")
            else:
                print("gun")
        else:
            print("gun")
    else:
        print("gun")
else:
    print("gundan")
    
'''
'''
import random
m=random.randrange(0,5)
n=eval(input("输入一个数字 踩踩他是谁>>"))
while(n!=m):
    if ( n > m ):
        print("太大了")
    else:
        print("太小了")
    n=eval(input("输入一个数字 踩踩他是谁>>"))
print("才对了")
'''




    
