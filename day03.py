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

#from __future__ import print_function
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(j,i,i*j),end=' ')
    print()

