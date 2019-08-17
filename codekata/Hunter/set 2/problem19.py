import itertools
n=int(input())
count=0
a=[int(i) for i in input().split()]
for i in range(n):
    for i in itertools.combinations(a,i):
        if sum(i) in a:
            print(i)
            count+=1
print(count)
    
4