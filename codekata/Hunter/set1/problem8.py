import itertools
n = int(input())
lst=[int(i) for i in input().split()]
res=itertools.combinations(lst,2)
lst1 = []
for i in res:
    if sum(i) in lst:
        print(i[0], i[1], sum(i))
        
    

