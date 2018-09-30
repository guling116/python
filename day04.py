'''
rate_init = 0.05
res = 10000
for i in range(10):
    res = res *(1 + rate_init)
print(res)
# a = 10000 * (1 + rate_init) ** 10
count = res
for i in range(1,4):
    res = res * (1 + rate_init) 
    count += res
print(count)


'''
#逻辑思想:
#-------
#	寻找n**3 一定会先比n**2找到n值
#	找到了之后，我们就不打印n**3找到的n值
#	使用count关闭打印n值，再继续去寻找n**2的n值
'''
n = 0.0
count = True
while 1:
    n = n + 1.0
    if n * n * n > 12000:
        if count:
            print('n**3', n - 1)
            count = False

    # print('hahah')
    if n * n >= 12000:
        print(n * n)
        print('n**2', n)
        break


def computeNum(rate, loanAmount, numYears):
    totalPayment = loanAmount * ((1+rate)**numYears)
    return totalPayment

loanAmount = eval(input('输入贷款总额：'))
numYears =  eval(input('输入贷款周期（年）：'))
for i in range(0, 25):
    rate = 0.05 + i*0.00125
    totalPay = computeNum(rate, loanAmount, numYears)
    print('利率为%f的月还款额为%f，总还款额为%f' %(rate, totalPay/60, totalPay))


    Joker:
totalSum = 0
for i in range(1, 98, 2):
    j = i + 2
    totalSum += i/j
    #print(('%d/%d' %(i, j)))
print('计算结果为：'+ str(totalSum))



Joker:
def computePai(precise):
    pai = 0
    for i in range(1, precise+1):
        pai += (-1)**(i+1)/(2*i-1)
    pai = 4 * pai
    return pai

for i in range(10000, 100000+1, 10000):
    print('i=%d时pi的计算结果为：%.20f' %(i, computePai(i)))
'''

import requests
def request(url):
    html=requests.get(url)
    print(html.text)
request('123.sogou.com')

