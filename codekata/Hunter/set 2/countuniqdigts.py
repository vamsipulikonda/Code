m,n=[int(i) for i in input().split()]
count=0

for i in range(m,n+1):
    a=(set(str(i)))
    if len(a)==len(str(i)):
        count+=1
print(count)