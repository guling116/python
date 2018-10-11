#1

'''
def check1(a):
    if a== '-':
        return False
    else:
        return True
def check2(b):
    if b.isdigit():
        return False
    else:
        return True
number = input("Please input the security number(ep:ddd-dd-dddd): ")
count = 0
for i in number:
    if count == 3 | count == 6:
        if check1(i):
            break
    else:
        if check2(i):
            break
    count += 1
if count == 11:
    print("Valid SSN")
else:
    print("Invalid SSN")
'''

#2
'''
def _find(a, b):
    for i in range(0, (len(b) - len(a))):
        c=''
        for j in range (0,len(a)):
            c += b[i+j]
        if a == c:
            return True
    return False
a = input("Please input the first string: ")
b = input("Please input the twice string: ")
if _find(a, b):
    print("The " + a + " is the sub string of the " + b)
else:
    print("The " + a + " is not the sub string of the " + b)
'''


#3
'''
def check1(a):
    if len(a) >= 8:
        return True
    return False
def check2(a):
    if a.isalnum():
        return True
    return False
def check3(a):
    count = 0
    for i in a:
        if i.isdigit():
            count += 1
    if count >= 2:
        return True
    else:
        return False
p = input("Please input the password: ")
if check1(p) & check2(p) & check3(p):
    print("valid password")
else:
    print("invalid password")
'''


#4
'''
def countLetters(s):
    count = 0
    for i in s:
        if i.isalpha():
            count += 1
    return count
s = input("Please input the string: ")
print("The alpha number of the stirng is " + str(countLetters(s)))
'''


#5
'''
def getNumber(s):
    for i in s:
        if i >= 'a' and i <= 'c':
            print('2',end = "")
        elif i >= 'd' and i<= 'f':
            print('3',end = "")
        elif i >= 'g' and i <= 'i':
            print('4', end = "")
        elif i >= 'j' and i <= 'l':
            print('5', end = "")
        elif i >= 'm' and i <= 'o':
            print('6', end = "")    
        elif i >= 'p' and i <= 's':
            print('7', end = "")
        elif i >= 't' and i <= 'v':
            print('8', end = "")
        elif i >= 'w' and i <= 'z':
            print('9', end = "")
        else:
            print(i,end="")
n = input("Please input your calling number: ")
getNumber(n.lower())
'''


#6
'''
def _reverse(s):
    c = ""
    i = len(s) - 1
    while(i>=0):
        c += s[i]
        i -= 1
    return c
s = input("shu ru zi fu chuan: ")
print("fanxiangwei" + _reverse(s))
'''

#7


def isValid(num):
    if not num.startswith('4') and not num.startswith('5') and not num.startswith('6') and not num.startswith('37'):
        print("The credit card number is invalid. ")
        return
    if len(num) < 13 or len(num) > 16:
        print("The credit card number is invalid. ")
        return
    sum = 0
    num = list(num)
    for i in range(len(num)):
        c = int(num[i])
        if i % 2 != 0:
            sum += c
        c *= 2
        if c >= 10:
            c = c % 10 + c // 10
        sum += c
    if sum % 10 == 0:
        print("The credit card number is valid. ")
    else:
        print("The credit card number is invalid. ")
s = input("Enter the credit card number: ")
isValid(s)





# _*_coding:utf8-
'''
def checkISBN(str_):
    str_list = list(str_)
    SUM = 0
    for i in range(len(str_list)):
        if i % 2 == 0:
            res = int(str_list[i]) * 3
        else:
            res = int(str_list[i])
        SUM += res
    RES = 10 - SUM % 10
    if RES == 10:
        RES = 0
    print(RES)
str_ = input('>>')
checkISBN(str_)
def checkCard(card_num):
    card_list = list(card_num) 
    Res = 0
    Res_2 = 0
    for i in range(len(card_list)):
        res = int(card_list[i]) * 2  
        if res >= 10:
            res_1 = res % 10  
            res_2 = res // 10
            res_3 = res_2 + res_1
            Res += res_3
        else:
            Res += res
        if i % 2 !=0: 
            Res_2 += int(card_list[i])
    RES = Res + Res_2
    if RES % 10 == 0:
        print('True')
    else:
        print('Flase')
card_num = '438857601840707'
checkCard(card_num)
# Deepcopy
# http://www.pythontutor.com/visualize.html#mode=display
import copy
a = [100,1,2,3,[1000,200]]
b =copy.deepcopy(a)
print(b)
a[4][0] = -1
print(b)
'''
