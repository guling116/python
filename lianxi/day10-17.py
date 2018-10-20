#编写平行四变形以*输出
for i in range(0,8):
    for j in range(8,i,-1):
        print(" ",end="")
    for a in range(0,i+(i+1)):
        print("*",end="")
    print()
for x in range(0,7):
    for c in range(0,x+1):
        print(" ",end="")
    for h in range(0,1):     #向右平移一个单位长度
        print(" ",end="")
    for d in range(7,x,-1):
        print("*",end="")
    for f in range(7,d,-1):
        print("*",end="")
    print()

'''
#用户输入一个输，判断这个数在1-10之间能否有被整除的数:
a=eval(input("输入一个数："))
for i in range(1,11):
    while 1:
         if a%i==0:
             print("存在")
    break
'''
'''
#智障程序
a=int(input("请输入一个数字："))
for i in range(1,11):
    if i%a==0:
        print("存在")
        break
if a>10:
    print("不存在")
'''



'''
#1,2,3,4 能组成多少个互不相同且无重复的三位数
b=0
for i in range(1,5):
    for j in range(1,5):
        for a in range(1,5):
            if i!=j | i!=j | a!=j:
                 print("{}{}{}".format(i,j,a))
                 b=b+1
print("一共有{}".format(b))
'''


#求1-100内的所有质数
sum=0
for i in range(2,101):
    a=True
    for j in range(2,i-1):
        if i%j==0:
            a=False
            break
    if a==True:
        sum=sum+i

        print(i)
print(sum)


#求两个数的最小公倍数，和最大共约数
s=0
z=0
r=0
x=0
y=0
a,b,c=eval(input("输入3个数："))
for i in range(2,101):
    while  a%i==0:
        s=i*i
        print("a{}".format(s))
        break
    while b%i==0:
        z=i*i
        print("b{}".format(z))
        
        break
#        print("r={}".format(r))
'''
if b%i==0:
        x=i*i
        print("x={}".format(x))
    if c%i==0:
        c=i*i
        print("c={}".format(c))
'''

    
        

