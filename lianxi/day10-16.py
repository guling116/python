#输出一到一百的所有奇数和与偶数和
a=0
b=0
for i in range(1,101):
    if i%2==0:
        a=a+i
        print("a={}".format(a))
    else:
        b=b+i
        print("b={}".format(b))
print("a={},b={}".format(a,b))


#输出十行十列的*
for i in range(1,11):
    for j in range(1,11):
        print("+",end="")
    print(" ")
print(i)

#输出一个直角三角形
for i in range(1,10):
    for j in range(1,i+1):
        print("+",end="")
    print()

#输出9乘9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        s=i*j
        print(j,"*",i,"=",s,end="")
    print()

'''
#每个班有五名同学，分别求出每个学生的3科成绩的平均值
for i in range(1,6):
    sum = 0
    for j in range(1,4):
        a=input("请输入地{}个同学第{}门成绩:".format(i,j))
        a=int(a)
        sum=sum+a
    sum=sum/j
    print("第{}名学生的平均成绩{}".format(i,sum))
print()
'''


'''
#附加(无聊的瞎便)
sum=0
for i in range(1,4):
    for j in range(1,4):
        a=input("{}楼{}房间".format(i,j))
        a=int(a)
        sum=sum+a
    sum=sum/j
    print("{}楼{}房间".format(i,sum))
print()
'''

'''
#画平行四变形
for i in range(0,8):
    for e in range(8,i,-1):
        print(" ",end="")
    for j in range(0,i+(i+1)):
        print("*",end="")
    for a in range(8,i,-1):
        print("×",end="")
    for b in range(8,a,-1):
        print("&",end="")
    print()
'''

#菱形
for i in range(0,8):
    for j in range(8,i,-1):
        print(" ",end="")
    for a in range(0,i+(i+1)):
        print("*",end="")
    print()
for b in range(0,8):
    for c in range(0,b+1):
        print(" ",end="")
    for d in range(8,b,-1):
        print("*",end="")
        for e in range(8,d,-7):
             print("*",end="")
    print()




