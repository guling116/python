#
'''
new text=""
for i in text:
    chr(ord(i)+1)
    new text = new text + 1'
    '''


'''
i=0
while(i<10):
    print("gid")
    i +=1
'''

#for i in "abcde":
#    print(i)
'''
a="abcde"
i=0
while(i<5):
    print(a[i])
    i +=1
'''
'''
import random
a=eval(input("shu ru yi ge shu :"))
n=random.randrange(0,5)
while(n!=a):
    print("zai cai ")
    a=eval(input("shu ru yi ge shu :"))
print("cai dui le")
   '''
'''
import random
a=eval(input("shu ru yi ge shu :"))
b=random.randrange(0,10)
if a==b :
    print("cai dui le")
else:
    while(a!=b):
        print("zai cai")
        a=eval(input("shu ru yi ge shu :"))
        if(a==b):
            print("cai dui le ")
        else:
            print("eorror")

'''

#range
#for i in range(0,9):
#    print(i)
'''
sum = 0
for i in range(1001):
    sum =sum+1
    print(i)
'''
'''

i=0
sum_= 0 
while(i<1001):
    sum_ +=i
    i +=1
    print(i)
'''

'''
i=1
sum_=0
while(sum_<10000):
    sum_ = sum_ +i
    i+=1
print(sum_)
'''


'''
i=0
sum_=0
for i in range(142):
      sum_=sum_+i
#     sum_ +=i
    print(sum_=sum_+i)
print(i,sum_)
'''
'''
#from __future__ import print_function
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(j,i,i*j),end=' ')
    print()
'''

#函数调用：
def abc(nu1,nu2,nu3):                   #输入函数的三个值
    return nu1,nu2,nu3                  #原本返回三个值
def acb(nu1,nu2,nu3):                   #括号里的可以写任意之值，                                                                       # 只做接受上个函数的三个值
    nu4=nu1**2
    nu5=nu2**2
    nu6=nu3**2
    return nu4,nu5,nu6                  #返回相乘之后的三个值
def cba(nu1,nu2,nu3,nu4,nu5,nu6):       #括号的值可以是任意，接受上面的六个值
    res1=nu4-nu1
    res2=nu5-nu2
    res3=nu6-nu3
    print(res1,res2,res3)
a,b,c=abc(3,6,9)                        #用a,b,c三个容器接受用户输入的三个数
q,w,e=acb(a,b,c)                        #用q,w,e三个容器接受相乘之后的三个数    
cba(a,b,c,q,w,e)                        #记住传参的函数！！！
                                        #记住传参的函数！！！
                                        #记住传参的函数！！！











