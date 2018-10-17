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

a=int(input("请输入一个数字："))
for i in range(1,11):
    if i%a==0:
        print("存在")
        break
if a>10:
    print("不存在")


