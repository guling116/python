'''
#3-1
b=0
c=0
while 1 :
    a=input("Enthe an integer, the input ends if it is :")
    if((a>0)|(a<0)):
        if a>0:
            b=a
        else:
            c=-a
    if(a==0):
        print("zheng shu {},fushu {},pingjunshu {}".format(b,c,(b+c)))
        break
'''


'''
#3-2
j = 0
for i in range(15):
    s = 10000+10000*0.05
    j = j + s
    if i==10:
        a = j
        print(a)
    if i == 11:
        b = j
        d = b-a
        print(d)
print(j-a)
'''
'''
#3-3
s=10000
for i in range(10):
    s=s+s*0.05
print(s)
n=s
for i in range(4):
    n=n+n*0.05
print(n)
'''
'''
#3-4
a=0
for i in range(100,1000):
    if(i%5==0 and i%6==0):
        a=a+1
        print("%3d" % i, end=" ")
        if(a%10==0):
            print(" ")

'''
'''
#3-5
import math
n=0.0
while 1:
    n = n+1.0
    if n*n*n<12000:
        print(n)
        break

    if n*n>=12000:
       print(n)
       break
'''


'''
#3-5
n=1
while(n<12000):
    if(n*n>12000):
        print(n)
        break
    n=n+1
s=1
while(s<12000):
    if(s*s*s>12000):
        print(s-1)
        break
    s=s+1
'''


'''
#3-6
p = eval(raw_input(">>"))
y = eval(raw_input(">>"))
n = 0.05
while n<8.125:
    n = n+0.125
    s = p*pow((1.0+n),1)
    print(s)
    m = s/12
    print(m)
'''


'''
#3-7
n=0
for i in range(1,50001):
    n=n+1/i
print(n)
s=50000
m=0
while(s>0):
    m=m+1/s
    s=s-1
print(m)
'''
'''
#3-8
a=1.0
b=3.0
sum1=0
while (a<=97):
    sum1=sum1+a/b
    a=a+2
    b=b+2
print(sum1)
'''
'''
#3-9
#_*_coding:utf8-
a=input(">>")
b=0
sum=0
for i in range(1,a+1):
    sum+=pow((-1),(a+1))/2*a-1
b=sum*4
print(b)
'''

'''
#3-9-2
n=0
for i in range(1,100000):
    n=n+pow((-1),i+1)/(2*i-1)
    if(i%10000==0):
        print(4*n)
'''
'''
#3-10

for i in range(1,10001):
    n=0
    for j in range(1,i/2+1):
        if(i%j==0):
            n=n+j
    if(n==i):
        print(i)
'''


'''
#3-11
a=0
for i in range(1,8):
    for j in range(i+1,8):
        print("sum {}".format((i)+(j)))
        a=a+1
print "sum",a
'''











