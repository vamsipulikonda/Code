n = int(input())
k=[]
lst = [int(i) for i in input().split()]
for i in range(len(lst)):
   
    if lst[i]%2 != 0 and i%2 == 0:
        print(lst[i], end=' ')
    if lst[i]%2 == 0 and i%2 != 0:
        print(lst[i], end=' ')
 