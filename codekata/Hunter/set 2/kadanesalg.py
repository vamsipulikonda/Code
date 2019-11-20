n=int(input())
k=[]

lst=[int(i) for i in input().split()]
for i in range(n+1):
    for j in range(i+1,n+1):
        k.append(sum(lst[i:j]))
    
print(max(k))
print(i,j)
    
