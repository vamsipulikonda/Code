"""order the input elements as (max1,min1,max2,min2....maxn,minn)"""

n=sorted([int(i) for i in input().split()])
temp=[]
while len(n)>0:
    a,b=max(n),min(n)
    temp.append(a)
    n.pop()
    temp.append(b)
    n.remove(b)
print(temp)