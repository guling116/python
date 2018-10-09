'''
#3-1
a,b=eval(input("Enter an integer, the input ends if it is "))
c=0
d=0
if (a>0):
    c=a
if (a<0):
    d=-a
print("c",c)
print("d",d)
'''

'''
s=0
j=0
o=0
while(1):
    a=int(input("Enter an integer,the input ends if it is 0:"))
    if((a>0)|(a<0)):
        s=s+a
        if(a>0):
            j=j+1
        else:
            o=o+1
    if(a==0):
        print("正数：%d,负数：%d,平均值：%.2f"%(j,o,1.0*s/(j+o)))
        break
'''
'''
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
 
print ("Good bye!")
'''


'''
# -*- coding: UTF-8 -*-

a=0
while (a<10):
    a=a+1
    if a%2==0:
        continue
    print("this is ",a)
print("jie shu")
'''
'''
#3-1
b=0
c=0
while(1):
    a=int(input("Enter an integer,the input ends if it is 0:"))
    if a<0:
        b=-a
    if a>0:
        c=a

    if a==0:
         print("zheng shu {},fu shu {},pingjunshu {}".format(c,b,(c+b)/2))
         break
'''


