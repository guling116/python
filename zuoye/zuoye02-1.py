'''
#EP-10
import random
a=random.randrange(0,100)
b=random.randrange(0,100)
n=eval(input("shu ru yi ge shu : "))
if(n==(a+b)):
    print(True)
else:
    print(False)
'''
'''
#EP-11
a=eval(input("Enter today's 0--6 : :"))
b=eval(input("Enter the number of day elapsed since today :"))
c=["Sun","Mo","Tuesday","Wed","Thursday","Firday","Saturday"]
if((a+b)%7==0):
    d=c[0]
elif((a+b)%7==1):
    d=c[1]
elif((a+b)%7==2):
    d=c[2]
elif((a+b)%7==3):
    d=c[3]
elif((a+b)%7==4):
    d=c[4]
elif((a+b)%7==5):
    d=c[5]
else:
    d=[6]
x=c[a]
print("Today is {} and the futher day is {}".format(x,d))
'''

'''
#EP-12
x,y,z=eval(input("shu ru san ge shu : "))
a=[x,y,z]
a.sort()
print(a)
'''
'''
#EP-13
a,b=eval(input("Enter weight and price for package 1 :"))
a1,b1=eval(input("Enter weight and price for package 2 :"))
if(b/a>b1/a1):
    print("package 2 has the batter pice")
elif(b/a==b1/a1):
    print("package 2 = 1")
else:
    print("package 1 has the batter pice")
'''


'''
#EP-14
a,b=input("shu ru yuefen he nianfen :")
if not (a==1)|(a==3)|(a==5)|(a==7)|(a==8)|(a==10)|(a==12):
    if not (a==4)|(a==6)|(a==9)|(a==11):
        if ((b%4==0&b%100!=0)|b%400==0) :
            print("29")
        else:
            print("28")
    else:
        print("30")
else:
    print("31")

'''
'''
a,b=input("shu ru yi ge yue he nian : ")
if (a==2):
    if((b%4==0&b%100!=0)|b%400==0):
    	print("29")
    else:
        print("28")
else:
    if(a==1)|(a==3)|(a==5)|(a==7)|(a==8)|(a==10)|(a==12):
    	print("31")
    else:
    	print("30")
print("The {}year and {}month have".format(b,a,))
'''

'''
#_*_ -coding:utf8-
import random
a=random.randint(0,1)
b=input("0 or 1 :")
if(a==b):
    print("cai dui le")
else:
    print("cai cuo le")
'''

'''
#3-8
import random
a=random.randint(0,2)
b=input("scissor(0) , rock(1), paper(2) :")
if (a==0)&(b==0):
    print("The computer is scissor,you are scissor.ping ju")
elif (a==0)&(b==1):
    print("THe computer is scissor,you are roke,you win")
elif (a==0)&(b==2):
    print("The computer is scissor,you are paper,It is a draw")
elif (a==1)&(b==0):
    print("The computer is rock,you are scissor,you fail")
elif (a==1)&(b==1):
    print("The computer is rock,you are rock,ping ju")
elif (a==1)&(b==2):
    print("The computer is rock,you are paper,you win")
elif (a==2)&(b==0):
    print("The computer is paper,you are scissor,you win")
elif (a==2)&(b==1):
    print("The computer is paper,you are rock,you fail")
elif(a==2)&(b==2):
    print("The computer is paper,you are paper,ping ju")

'''

'''
#3-10
import random
a=['Ace',2,3,4,5,6,7,8,9,'Jack','Queen','King']
b=['meihua','hongtao','fangpian','heitao']
c=random.choice(a)
d=random.choice(b)
print("The card picked is the {} of {}".format(c,d))
'''

'''
#3-11
a=input("shu ru yi ge san wei shu ")
b=a%100%10
c=a%100/10
d=a/100
if (b==d)|(b==c==d) :
    print("{} is a palindrome".format(a))
else:
    print("{} is not a palindrome".format(a))

'''
'''
#3-12
a,b,c=input("Enter three edges :")
if (a+b>c) and (a+c>b) and (b+c>a):
    s=a+b+c
    print("The perimeter is {}".format(s))
else:
    print("error")
'''






