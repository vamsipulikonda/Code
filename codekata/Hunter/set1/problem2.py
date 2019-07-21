import itertools
n=int(input())
a=[]
lst=[int(i)for i in input().split()]
res=itertools.permutations(lst, n)
for i in res:
   
    a.append(int(''.join([str(j) for j in i])))
print(max(a))
