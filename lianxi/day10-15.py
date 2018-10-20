'''
#编写9×9乘法口诀
for i in range(1,10):
    for j in range(1,i+1):
        s=i*j
        print(j,"*",i,"=",s,end="")
    print("")

#输出十行十列
for i in range(1,11):
    for j in range(1,11):

         print('x',end="")
    print()

#输出1到100之间的偶数和与奇数和
a=0
b=0
for i in range(1,100):
    if i%2==0:
        a=a+i
        print("a={}".format(a))
    else:
        b=b+i
        print("b={}".format(b))
print("a={},b={}".format(a,b))

#输出直角三角形
a=0
b=0
for i in range(1,6):
    for j in range(1,i+1):
        print("x",end="")
    print("")


#以后在写（不会）：
#菲波那契数列（第一种）
a=0
b=1
c=a+b
print(a,b)
while c < 100:
    print(c,end="")
    a=b
    b=c
    c=a+b
print() 


#每个班有五名同学，分别求每个学生的3科成绩的平均值
for i in range(1,6):
    sum=0
    for j in range(1,4):
        a=input("请输入第%d个学生",str(j),"门成绩:"%i)
        s=int(s)
        sum=sum+j
    print("第",i,"同学的总成绩",sum)
print()
'''

name_1="niu  "
name_2="bai chao "
name_3=name_1 +" "+ name_2
print(name_3)
print(name_3.title())
print(name_3.lower())
print("\nhello," + name_3.upper() + "\n!")
messge= "hello, " + name_3.upper() + "!"
print(messge)
print("\npython\n")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print(name_3.rstrip())





