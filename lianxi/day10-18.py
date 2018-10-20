a= 23
say="hello "+str(a)+" word"
print(say)
title=["abc","def","MNF","aaa"]
print(title[0])
print(title[1].title())
print(title[2].lower())
a="this is a "+(title[-1].title())+"."
print(a)
title[0]="ccc"
print(title)
title.append("bbb")
print(title)
title.append("ddd")
print(title)
c=[]
c.append("aaa")
c.append("bbb")
c.append("ccc")
print(c)
c.insert(2,"fff")
print(c)
d=c.pop()
print(d,c)
print("aaa"+d+"!")
print("aaa"+c.pop(1)+"!")
print(c)
c.remove("fff")
print(c)
print(title)
title.sort()
title.sort(reverse=True)
print(title)
len(c)
