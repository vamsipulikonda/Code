"""
5
2 5 6 8 10
cond:form(x,y,z) with constrains
i<j<k
y-x=z-x
op:3(no of elements with possible condition)
"""
import itertools
n=input()
lst=[int(i) for i in input().split()]
count=0
for i in itertools.combinations(lst,3):
    if i[0]<i[1]<i[2] and i[1]-i[0]==i[2]-i[1]:
        print(i)
        count+=1
print(count)