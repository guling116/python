#3-1
b=0
c=0
while 1 :
    a=input("Enthe an integer, the input ends if it is :")
    if((a>0)|(a<0)):
        if a>0:
            b=a
        else:
            c=-a
    if(a==0):
        print("zheng shu {},fushu {},pingjunshu {}".format(b,c,(b+c)))
        break
