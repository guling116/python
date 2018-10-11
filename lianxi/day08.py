# url="http://www.baidu.com/?page=/wd=xiaopangzi"
'''
url1="www.baidu.com/?page="
url2="wd=xiaopangzi"
while(1):
    for i in range(1,100):
        print(url1,i,url2)
       i=i+1 
    break
         
for i in range(100):
    part1=www.baidu.com/?page=
    res = part1 + 
'''
'''
A1=[1,1,1,1,1,2,2,2,2,2,3]
a1=[]
for i in A1:
    if i not in a1:
        a1.append(i)
print a1

#A2=[1,2,3]
#A2.append(10)
#print A2
'''
'''
a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
a4.sort(key=lambda x:x[2][1])
print(a4)
'''
'''
t=(1,2,3,7,9,0,5)
print(t[ : -1])
'''
'''
a=0
b=0
while a < 10 :
    a=a+1
    print("a= {}".format(a))
    if a%10==0:
        print("")
print(a)
'''
'''
i=0
sum=0
while i<100:
    i=i+1
#    if i%2==0:
    sum=i+sum
    print("i={},sum={}".format(i,sum))
'''
'''
#shu chu 1-100 zhi jian de ou shu he
i=0
sum=0
while i<=100:
    i+=2
    sum=sum+i 
print(sum)
'''
'''
#1-100(while xun hua ) ji shu he he ou shu he shu chu
i=0
sum=0
a=0
while i<100:
    i=i+1
    if i%2==0:
        sum=sum+i
    else:
        a=a+i
print(sum,a)
'''
'''
# 1-100(for xun huan) ji shu he he ou shu he shu chu
sum=0
a=0
for i in range(1,101):
    if i%2==0:
        sum=sum+i
    else:
        a=a+i
print(sum,a)
'''
#for i in range(1,100,2):
#    print(i,end="\t")


# shu chu 10 hang 10 lie de *
#for i in range(1,11):
#    for j in range(1,j):
#         print(i,j)
for i in range(1,11):
    for j in range(1,11):
        print("*")
    print()







